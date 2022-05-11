import ctypes
import importlib
import inspect
import sys

import pandas as pd
from loguru import logger
from PySide6 import QtGui
from PySide6.QtCore import QDate, QObject, Signal
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget
from quant.core.worker import Config, Worker, WorkerTimer
from quant.utils.thread_util import thread_async_raise
from sqlalchemy import column

from .widgets.MainForm import Ui_MainForm


class Stream(QObject):
    _log = Signal(str)

    def write(self, text):
        self._log.emit(str(text))

    def flush(self):
        QApplication.processEvents()


class MainForm(QWidget, Ui_MainForm):
    def __init__(self):
        super().__init__()

        self.gui = Ui_MainForm()
        self.gui.setupUi(self)

        # Log
        self.stream = Stream()
        self.stream._log.connect(self.log)

        sys.stdout = self.stream
        sys.stderr = self.stream

        logger.add(self.stream, format="{time:YYYY-MM-DD HH:mm:ss} - {message}", level="INFO")

        self.gui.textEdit_Log.document().setMaximumBlockCount(4096)

        # Button
        self.gui.pushButton_DownloadSymbols.clicked.connect(self.download_symbols)
        self.gui.pushButton_LoadSymbols.clicked.connect(self.load_symbols)
        self.gui.pushButton_SetSavePath.clicked.connect(self.set_save_path)

        self.gui.pushButton_DownloaderStart.clicked.connect(self.start)
        self.gui.pushButton_DownloaderStop.clicked.connect(self.stop)

        self.gui.pushButton_TimerStart.clicked.connect(self.timer_start)
        self.gui.pushButton_TimerStop.clicked.connect(self.timer_stop)

        self.symbols = []
        self.save_path = ''
        self.worker_thread = None
        self.worker_timer = None

        self.gui.dateEdit_EndDate.setDate(QDate.currentDate())

        logger.info('Welcome to use Binance Downloader.')

    def log(self, text):
        if '\r' in text:
            text = text.replace('\r', '').rstrip()
            cursor = self.gui.textEdit_Log.textCursor()
            # cursor.movePosition(QtGui.QTextCursor.End)
            cursor.select(QtGui.QTextCursor.BlockUnderCursor)
            cursor.removeSelectedText()
            cursor.insertBlock()
            self.gui.textEdit_Log.setTextCursor(cursor)

        self.gui.textEdit_Log.insertPlainText(text)
        self.gui.textEdit_Log.moveCursor(QtGui.QTextCursor.End)

    def download_symbols(self):

        if self.gui.checkBox_spot.isChecked():
            logger.info('download spot symbols...')
            utility = importlib.import_module('quant.binance.python.utility')
            symbols = utility.get_all_symbols(self.gui.checkBox_spot.text())
            symbols_df = pd.DataFrame(symbols, columns=['Symbol'])
            symbols_df.sort_values(by='Symbol', axis=0, ascending=True, inplace=True)
            symbols_file_path = QFileDialog.getSaveFileName(self, 'Please Choose Save Path',
                                                            f'./symbols_{self.gui.checkBox_spot.text()}.csv', 'csv(*.csv)')
            if symbols_file_path[0] != '':
                symbols_df.to_csv(symbols_file_path[0], index=False, header=False)
                logger.info(
                    f'{len(symbols)} symbols({self.gui.checkBox_spot.text()}) have been saved to: {symbols_file_path[0]}')

        if self.gui.checkBox_um.isChecked():
            logger.info('download futures(um) symbols...')
            utility = importlib.import_module('quant.binance.python.utility')
            symbols = utility.get_all_symbols(self.gui.checkBox_um.text())
            symbols_df = pd.DataFrame(symbols, columns=['Symbol'])
            symbols_df.sort_values(by='Symbol', axis=0, ascending=True, inplace=True)
            symbols_file_path = QFileDialog.getSaveFileName(self, 'Please Choose Save Path',
                                                            f'./symbols_{self.gui.checkBox_um.text()}.csv', 'csv(*.csv)')
            if symbols_file_path[0] != '':
                symbols_df.to_csv(symbols_file_path[0], index=False, header=False)
                logger.info(f'{len(symbols)} symbols({self.gui.checkBox_um.text()}) have been saved to: {symbols_file_path[0]}')

        if self.gui.checkBox_cm.isChecked():
            logger.info('download futures(cm) symbols...')
            utility = importlib.import_module('quant.binance.python.utility')
            symbols = utility.get_all_symbols(self.gui.checkBox_cm.text())
            symbols_df = pd.DataFrame(symbols, columns=['Symbol'])
            symbols_df.sort_values(by='Symbol', axis=0, ascending=True, inplace=True)
            symbols_file_path = QFileDialog.getSaveFileName(self, 'Please Choose Save Path',
                                                            f'./symbols_{self.gui.checkBox_cm.text()}.csv', 'csv(*.csv)')
            if symbols_file_path[0] != '':
                symbols_df.to_csv(symbols_file_path[0], index=False, header=False)
                logger.info(f'{len(symbols)} symbols({self.gui.checkBox_cm.text()}) have been saved to: {symbols_file_path[0]}')

    def load_symbols(self):
        logger.info('load symbols...')
        symbols_file_path = QFileDialog.getOpenFileName(self, 'Please Choose Symbols File', '.', 'csv(*.csv *.*')
        if symbols_file_path[0] != '':
            symbols_df = pd.read_csv(symbols_file_path[0], index_col=None, header=None, names=['Symbol'], skip_blank_lines=True)
            logger.info(symbols_df)
            self.symbols = symbols_df['Symbol'].values.tolist()

    def set_save_path(self):
        self.save_path = QFileDialog.getExistingDirectory(self, 'Please Choose Save Path', ".")
        logger.info(f'set save path: {self.save_path}')

    def generate_config(self):

        if len(self.symbols) == 0:
            logger.info('please load symbols at first')
            return None

        if len(self.save_path) == 0:
            logger.info('please set save path at first')
            return None

        trading_type_list = []
        if self.gui.checkBox_spot.isChecked():
            trading_type_list.append(self.gui.checkBox_spot.text())
        if self.gui.checkBox_um.isChecked():
            trading_type_list.append(self.gui.checkBox_um.text())
        if self.gui.checkBox_cm.isChecked():
            trading_type_list.append(self.gui.checkBox_cm.text())

        data_type_list = []
        if self.gui.checkBox_Kline.isChecked():
            data_type_list.append(self.gui.checkBox_Kline.text())
        if self.gui.checkBox_AggTrade.isChecked():
            data_type_list.append(self.gui.checkBox_AggTrade.text())
        if self.gui.checkBox_Trade.isChecked():
            data_type_list.append(self.gui.checkBox_Trade.text())

        interval_list = []
        if self.gui.checkBox_1m.isChecked():
            interval_list.append('1m')
        if self.gui.checkBox_1h.isChecked():
            interval_list.append('1h')
        if self.gui.checkBox_1d.isChecked():
            interval_list.append('1d')

        config = Config(trading_type_list, self.symbols, data_type_list, interval_list,
                        self.gui.dateEdit_StartDate.date().toString('yyyy-MM-dd'),
                        self.gui.dateEdit_EndDate.date().toString('yyyy-MM-dd'), self.save_path)

        return config

    def start(self):
        logger.info('start worker thread...')

        config = self.generate_config()
        print(config)

        self.worker_thread = Worker(config)
        self.worker_thread.start()

    def stop(self):
        logger.info('stop worker thread...')
        thread_async_raise(self.worker_thread.ident, SystemExit)

    def timer_start(self):
        logger.info('start timer...')

        config = self.generate_config()
        print(config)

        self.worker_timer = WorkerTimer(config)
        self.worker_timer.start()

    def timer_stop(self):
        logger.info('stop timer...')
        if self.worker_timer is not None:
            self.worker_timer.stop()
