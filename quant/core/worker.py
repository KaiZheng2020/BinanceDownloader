import importlib
import time
from datetime import date, datetime, timedelta
from threading import Thread, Timer

import pandas as pd
from loguru import logger
from sympy import N
from tabulate import tabulate


class Config():
    def __init__(self,
                 trading_type_list,
                 symbol_list,
                 data_type_list,
                 interval_list,
                 date_start,
                 date_end,
                 save_path,
                 proxy=None):

        self.trading_type_list = trading_type_list
        self.symbol_list = symbol_list
        self.data_type_list = data_type_list
        self.interval_list = interval_list
        self.date_start = date_start
        self.date_end = date_end
        self.save_path = save_path
        self.proxy = proxy

    def __str__(self):
        if len(self.symbol_list) > 5:
            symbols = len(self.symbol_list)
        else:
            symbols = self.symbol_list

        table = [
            ['trading type', self.trading_type_list],
            ['symbols', symbols],
            ['data type', self.data_type_list],
            ['interval', self.interval_list],
            ['start date', self.date_start],
            ['end date', self.date_end],
            ['save path', self.save_path],
            ['proxy', self.proxy],
        ]

        return tabulate(table, tablefmt='grid')


def download(config: Config):

    for trading_type in config.trading_type_list:
        for data_type in config.data_type_list:
            for symbol in config.symbol_list:

                try:
                    dates = pd.date_range(
                        start=config.date_start,
                        end=config.date_end,
                    ).to_pydatetime().tolist()

                    dates = [date.strftime("%Y-%m-%d") for date in dates]

                    if data_type == 'kline':
                        downloader = importlib.import_module('quant.binance.python.download-kline')
                        downloader.download_daily_klines(trading_type, [symbol], 1, config.interval_list, dates,
                                                         config.date_start, config.date_end, config.save_path, False)

                    elif data_type == 'aggTrade':
                        downloader = importlib.import_module('quant.binance.python.download-aggTrade')
                        downloader.download_daily_aggTrades(trading_type, [symbol], 1, dates, config.date_start,
                                                            config.date_end, self.config.save_path, False)
                    elif data_type == 'trade':
                        downloader = importlib.import_module('quant.binance.python.download-trade')
                        downloader.download_daily_trades(trading_type, [symbol], 1, dates, config.date_start, config.date_end,
                                                         config.save_path, False)
                    else:
                        logger.error(f'unsupport data type: {data_type}')

                except Exception as ex:
                    logger.error(ex)


class Worker(Thread):
    def __init__(self, config):
        super(Worker, self).__init__()

        self.config = config
        self.thread_flag = False

    def run(self):
        download(self.config)
        logger.info(f'worker thread has exited.')


class WorkerTimer(Thread):
    def __init__(self, config, clock):
        super(Worker, self).__init__()

        self.config = config
        self.thread_flag = False
        self.clock = clock

    def run(self):
        self.thread_flag = True

        while self.thread_flag:

            if datetime.now().hour == self.clock:
                self.config.date_start = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
                self.config.date_end = date.today().strftime("%Y-%m-%d")
                download(self.config)

            time.sleep(60 * 60)

        logger.info(f'worker thread has exited.')

    def stop(self):
        self.thread_flag = False
        logger.info(f'stop worker thread...')
