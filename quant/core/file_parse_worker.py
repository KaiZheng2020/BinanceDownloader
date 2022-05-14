import glob
import multiprocessing
import os
from dataclasses import replace
from threading import Thread

import pandas as pd
from loguru import logger
from multiprocess import Pool
from quant.utils.file_util import untargz, unzip
from sympy import N
from tabulate import tabulate
from tqdm import tqdm


class FileParseConfig():
    def __init__(self, src_path, des_path, parse_zip_flag, parse_csv_flag, parse_feather_flag, auto_parse_file_type_flag,
                 save_file_csv_flag, save_file_feather_flag):

        self.src_path = src_path
        self.des_path = des_path
        self.parse_zip_flag = parse_zip_flag
        self.parse_csv_flag = parse_csv_flag
        self.parse_feather_flag = parse_feather_flag
        self.auto_parse_file_type_flag = auto_parse_file_type_flag
        self.save_file_csv_flag = save_file_csv_flag
        self.save_file_feather_flag = save_file_feather_flag

    def __str__(self):

        table = [['Src Path', self.src_path], ['Des Path', self.des_path], ['Parse Zip File', self.parse_zip_flag],
                 ['Parse CSV File', self.parse_csv_flag], ['Parse Feather File', self.parse_feather_flag],
                 ['Auto Parse File Type', self.auto_parse_file_type_flag], ['Save CSV File', self.save_file_csv_flag],
                 ['Save Feather File', self.save_file_feather_flag]]

        return tabulate(table, tablefmt='grid')


class FileParseWorker(Thread):
    def __init__(self, config: FileParseConfig):
        super(FileParseWorker, self).__init__()

        self.config = config

    def run(self):
        logger.info(self.config)

        if self.config.parse_zip_flag:
            file_list = glob.glob(f'{self.config.src_path}/**/*.zip', recursive=True)
            logger.info(f'unzip {len(file_list)} zip files.')
            for file in file_list:
                try:
                    unzip(file)
                except Exception as ex:
                    logger.error(f'unzip fails: {file}')

        for root, dirs, files in os.walk(self.config.src_path):
            content_df = pd.DataFrame()
            content_list = []
            for file in files:
                if self.config.parse_csv_flag and '.csv' in file:
                    content_list.append(pd.read_csv(os.path.join(root, file), header=None))
                if self.config.parse_feather_flag and '.feather' in file:
                    content_list.append(pd.read_csv(os.path.join(root, file), header=None))

            if len(content_list) > 0:

                content_df = pd.concat(content_list)
                save_path = os.path.join(self.config.des_path, root[len(self.config.src_path) + 1:])
                if self.config.auto_parse_file_type_flag:
                    if 'kline' in root:
                        content_df.columns = [
                            'datetime', 'open', 'high', 'low', 'close', 'volume', 'closetime', 'quote_asset_volume',
                            'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
                        ]

                        content_df['closetime'] = pd.to_datetime(content_df['datetime'], unit='ms')

                    elif 'aggTrade' in root:
                        content_df.columns = [
                            'trade_id', 'price', 'quantity', 'first_trade_id', 'last_trade_id', 'datetime',
                            'was_the_buyer_the_maker'
                        ]

                    elif 'trade' in root:
                        content_df.columns = ['trade_id', 'price', 'qty', 'quote_qty', 'datetime', 'is_buyer_maker']

                content_df['datetime'] = pd.to_datetime(content_df['datetime'], unit='ms')
                content_df.set_index('datetime', inplace=True)
                content_df.sort_index(axis=0, inplace=True)
                content_df.reset_index(inplace=True)

                if not os.path.exists(save_path):
                    os.makedirs(save_path)

                if self.config.save_file_csv_flag:
                    save_csv_path = os.path.join(save_path, 'results.csv')
                    content_df.to_csv(save_csv_path, index=False)
                    print(save_csv_path)
                if self.config.save_file_feather_flag:
                    save_feather_path = os.path.join(save_path, 'results.feather')
                    content_df.to_feather(save_feather_path)
                    print(save_feather_path)

        logger.info(f'worker thread has exited.')
