import hashlib
import hmac
import json
import math
import multiprocessing
import os
import tarfile
import time
from glob import glob
from urllib.parse import urlencode

import numpy as np
import pandas as pd
import requests
from loguru import logger
from multiprocess import Pool
from tqdm import tqdm

from .. import g_config
from .utils import datetime2unix, unix2datetime

binance_api_url = g_config['binance']['binance_api_url']
binance_api_key = g_config['binance']['binance_api_key']
binance_secret_key = g_config['binance']['binance_secret_key']


def _sign(params={}):
    data = params.copy()
    ts = str(int(1000 * time.time()))
    data.update({"timestamp": ts})
    h = urlencode(data)
    b = bytearray()
    b.extend(binance_secret_key.encode())
    signature = hmac.new(b, msg=h.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    sig = {"signature": signature}
    return data, sig


def _post(path, params={}):
    sign = _sign(params)
    query = urlencode(sign[0]) + "&" + urlencode(sign[1])
    url = "%s?%s" % (path, query)
    header = {"X-MBX-APIKEY": binance_api_key}
    p = requests.post(url, headers=header, timeout=30, verify=True)
    # logger.info(p.headers)
    return p


def _get(path, params):
    sign = _sign(params)
    query = urlencode(sign[0]) + "&" + urlencode(sign[1])
    url = "%s?%s" % (path, query)
    header = {"X-MBX-APIKEY": binance_api_key}
    p = requests.get(url, headers=header, timeout=30, verify=True)

    # logger.info(p.headers)
    return p


def get_history_data_id(symbol, data_type, start_time, end_time):
    path_query = f'{binance_api_url}/futuresHistDataId'
    params = {
        "symbol": symbol,
        "startTime": datetime2unix(start_time),
        "endTime": datetime2unix(end_time),
        "dataType": data_type
    }
    result = _post(path_query, params).json()
    if 'id' not in result:
        raise ConnectionError(result)
    id = result['id']
    logger.info(f'data id: {id} ({start_time}, {end_time})')
    return id


def get_history_data_url(id):
    while True:

        try:
            path = f'{binance_api_url}/downloadLink'
            params = {"downloadId": id}
            result = _get(path, params).json()
        except Exception as ex:
            logger.info(ex)
            time.sleep(600)

        if 'expirationTime' in result:
            expiration_time = unix2datetime(result['expirationTime'] * 1000)
            link = result['link']
            logger.info(f'Link is OK! ExpirationTime: {expiration_time} Link: {link}')
            return link
        elif 'status' in result:
            logger.info(result)
            break
        else:
            logger.info(result)
            time.sleep(600)


def download_history_data_file(url, file_path):
    req = requests.get(url, stream=True)
    total_size = int(req.headers.get('content-length', 0))
    block_size = 1024 * 1024
    wrote = 0
    with open(file_path, 'wb') as f:
        for data in tqdm(req.iter_content(block_size), total=math.ceil(total_size // block_size), unit='MB', unit_scale=True):
            wrote = wrote + len(data)
            f.write(data)
    if total_size != 0 and wrote != total_size:
        logger.error(f'ERROR, total_size: {total_size} wrote:{wrote}')
    else:
        logger.info(f'Finished, {file_path}')


def untargz(targz_file, remove_flag=False):
    path = os.path.dirname(targz_file)
    targz = tarfile.open(targz_file)
    targz.extractall(path=path)
    targz.close()
    if remove_flag:
        os.remove(targz_file)


def csv_to_feather_s_depth(file, remove_flag=False):
    df = pd.read_csv(file, dtype=str, comment='#')
    df.rename(columns={'ts': 'datetime'}, inplace=True)
    df.drop('last_update_id', axis=1, inplace=True)
    df.to_feather(file.replace('.csv', '.feather'))
    if remove_flag:
        os.remove(file)


def csv_to_feather_t_trade(file, remove_flag=False):
    df = pd.read_csv(file,
                     names=['id', 'symbol', 'price', 'qty', 'quoteQty', 'datetime', 'isBuyerMaker'],
                     dtype=str,
                     comment='#')
    df.drop('id', axis=1, inplace=True)
    df.to_feather(file.replace('.csv', '.feather'))
    if remove_flag:
        os.remove(file)


def download_s_depth(symbol, save_path, start_time, end_time):
    data_id = get_history_data_id(symbol, 'S_DEPTH', start_time, end_time)
    url = get_history_data_url(data_id)
    start_time = start_time.replace('-', '')
    end_time = end_time.replace('-', '')
    file_name = rf'{save_path}/{symbol}_S_DEPTH_{start_time}_{end_time}.tar.gz'
    download_history_data_file(url, file_name)
    untargz(file_name, remove_flag=False)

    file_list = glob(save_path + '/*.csv')
    if (len(file_list) == 0):
        raise FileNotFoundError(f'cannot find csv file: {save_path}')

    NUM_USABLE_CPU = max(multiprocessing.cpu_count() - 2, 1)
    workers = min(NUM_USABLE_CPU, len(file_list))

    with Pool(processes=workers) as p:
        results = list(tqdm(p.imap(lambda x: csv_to_feather_s_depth(x, True), file_list), total=len(file_list)))


def download_t_trade(symbol, save_path, start_time, end_time):
    data_id = get_history_data_id(symbol, 'T_TRADE', start_time, end_time)
    url = get_history_data_url(data_id)
    start_time = start_time.replace('-', '')
    end_time = end_time.replace('-', '')
    file_name = rf'{save_path}/{symbol}_T_TRADE_{start_time}_{end_time}.tar.gz'
    download_history_data_file(url, file_name)
    untargz(file_name, remove_flag=False)

    file_list = glob(save_path + '/*.csv')
    if (len(file_list) == 0):
        raise FileNotFoundError(f'cannot find csv file: {save_path}')

    NUM_USABLE_CPU = max(multiprocessing.cpu_count() - 2, 1)
    workers = min(NUM_USABLE_CPU, len(file_list))

    with Pool(processes=workers) as p:
        results = list(tqdm(p.imap(lambda x: csv_to_feather_t_trade(x, True), file_list), total=len(file_list)))
