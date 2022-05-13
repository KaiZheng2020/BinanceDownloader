import ctypes
import importlib
import inspect
import sys

import pandas as pd
from loguru import logger
from PySide6 import QtGui
from PySide6.QtCore import QDate, QObject, Signal
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget
from quant.core.file_parse_worker import FileParseConfig, FileParseWorker
from quant.core.history_download_worker import (HistoryDownloadConfig, HistoryDownloadTimer, HistoryDownloadWorker)
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

        logger.add(self.stream, format="{time:YYYY-MM-DD HH:mm:ss} {level} - {message}", level="INFO")

        self.gui.textEdit_Log.document().setMaximumBlockCount(4096)

        # Button
        self.gui.pushButton_DownloadSymbols.clicked.connect(self.download_symbols)
        self.gui.pushButton_LoadSymbols.clicked.connect(self.load_symbols)
        self.gui.pushButton_SetSavePath.clicked.connect(self.set_save_path)

        self.gui.pushButton_DownloaderStart.clicked.connect(self.history_download_thread_start)
        self.gui.pushButton_DownloaderStop.clicked.connect(self.history_download_thread_stop)

        self.gui.pushButton_TimerStart.clicked.connect(self.history_download_timer_start)
        self.gui.pushButton_TimerStop.clicked.connect(self.history_download_timer_stop)

        self.gui.pushButton_SetSrcDir.clicked.connect(self.set_src_dir)
        self.gui.pushButton_SetDesDir.clicked.connect(self.set_des_dir)
        self.gui.pushButton_ParseStart.clicked.connect(self.parse_start)
        self.gui.pushButton_ParseStop.clicked.connect(self.parse_stop)

        # History Download Variables
        self.history_download_symbols = []
        self.history_download_save_path = ''
        self.history_download_thread = None
        self.history_download_timer = None

        # File Parse Variables
        self.file_parse_thread = None

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

    # History Download Functions

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
            self.history_download_symbols = symbols_df['Symbol'].values.tolist()

    def set_save_path(self):
        self.history_download_save_path = QFileDialog.getExistingDirectory(self, 'Please Choose Save Path', ".")
        logger.info(f'set save path: {self.history_download_save_path}')

    def generate_history_download_config(self):

        if len(self.history_download_symbols) == 0:
            logger.info('please load symbols at first')
            return None

        if len(self.history_download_save_path) == 0:
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

        proxy = None
        if self.gui.checkBox_Proxy.isChecked():
            proxy = self.gui.lineEdit_Proxy.text()

        config = HistoryDownloadConfig(trading_type_list, self.history_download_symbols, data_type_list, interval_list,
                                       self.gui.dateEdit_StartDate.date().toString('yyyy-MM-dd'),
                                       self.gui.dateEdit_EndDate.date().toString('yyyy-MM-dd'), self.history_download_save_path,
                                       proxy)

        return config

    def history_download_thread_start(self):
        logger.info('start worker thread...')

        config = self.generate_history_download_config()

        if config == None:
            logger.error('history download config is None.')

        else:
            logger.info(config)

            self.history_download_thread = HistoryDownloadWorker(config)
            self.history_download_thread.start()

    def history_download_thread_stop(self):
        logger.info('stop worker thread...')
        thread_async_raise(self.history_download_thread.ident, SystemExit)

    def history_download_timer_start(self):
        logger.info('start timer...')

        config = self.generate_history_download_config()
        print(config)

        self.history_download_timer = HistoryDownloadTimer(config)
        self.history_download_timer.start()

    def history_download_timer_stop(self):
        logger.info('stop timer...')
        if self.history_download_timer is not None:
            self.history_download_timer.stop()

    # File Parse Functions

    def set_src_dir(self):
        self.src_path = QFileDialog.getExistingDirectory(self, 'Please Choose Src Path', ".")
        self.gui.lineEdit_SrcDir.setText(self.src_path)

        if self.gui.radioButton_Kline.text() in self.src_path:
            self.gui.radioButton_Kline.setChecked(True)
        elif self.gui.radioButton_AggTrade.text() in self.src_path:
            self.gui.radioButton_AggTrade.setChecked(True)
        elif self.gui.radioButton_Trade.text() in self.src_path:
            self.gui.radioButton_Trade.setChecked(True)
        else:
            self.gui.radioButton_None.setChecked(True)

        logger.info(f'set src path: {self.src_path}')

    def set_des_dir(self):
        self.des_path = QFileDialog.getExistingDirectory(self, 'Please Choose Des Path', ".")
        self.gui.lineEdit_DesDir.setText(self.des_path)
        logger.info(f'set des path: {self.des_path}')

    def generate_file_parse_config(self):
        if len(self.src_path) == 0:
            logger.error('please set src path at first.')
            return None

        if len(self.des_path) == 0:
            logger.error('please set des path at first.')
            return None

        src_path = self.gui.lineEdit_SrcDir.text()
        des_path = self.gui.lineEdit_DesDir.text()
        parse_zip_flag = self.gui.checkBox_ParseZIP.isChecked()
        parse_csv_flag = self.gui.checkBox_ParseCSV.isChecked()
        parse_feather_flag = self.gui.checkBox_ParseFeather.isChecked()

        if self.gui.radioButton_Kline.isChecked():
            parse_file_type = 'kline'
        elif self.gui.radioButton_AggTrade.isChecked():
            parse_file_type = 'aggTrade'
        elif self.gui.radioButton_Trade.isChecked():
            parse_file_type = 'trade'
        else:
            parse_file_type = 'none'

        save_file_csv_flag = self.gui.checkBox_SaveCSV.isChecked()
        save_file_feather_flag = self.gui.checkBox_SaveFeather.isChecked()

        return FileParseConfig(src_path, des_path, parse_zip_flag, parse_csv_flag, parse_feather_flag, parse_file_type,
                               save_file_csv_flag, save_file_feather_flag)

    def parse_start(self):
        config = self.generate_file_parse_config()
        self.file_parse_thread = FileParseWorker(config)
        self.file_parse_thread.start()

    def parse_stop(self):
        logger.info('stop worker thread...')
        thread_async_raise(self.file_parse_thread.ident, SystemExit)
