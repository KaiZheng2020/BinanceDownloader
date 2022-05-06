import calendar
import copy
import re
import time
from datetime import datetime, timedelta, timezone, tzinfo
from glob import glob
from typing import Text, Union

import numpy as np
import pandas as pd
from dateutil.parser import parse
from loguru import logger
from pandas import DataFrame, Series


def date_range(begin, end):
    dates = []
    dt_begin = datetime.strptime(begin, '%Y-%m-%d')
    dt_end = datetime.strptime(end, '%Y-%m-%d')
    while dt_begin <= dt_end:
        dates.append(dt_begin.strftime('%Y%m%d'))
        dt_begin = dt_begin + timedelta(1)
    return dates


def month_range(begin, end):

    dates = []
    begin = datetime.strptime(begin, '%Y-%m-%d')
    end = datetime.strptime(end, '%Y-%m-%d')

    month_num = (end.year - begin.year) * 12 + end.month - begin.month
    year = begin.year
    month = begin.month

    for m in range(month_num + 1):
        dates.append(f'{year}-{str(month).zfill(2)}')
        month += 1
        if month > 12:
            month = 1
            year += 1

    return dates


def month_last_day(year, month):
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)
    return monthRange


def get_file_list_by_date_range(path, begin, end):
    file_list = []
    path_list = glob(path + '/*')
    dates = date_range(begin, end)
    for date in dates:
        file_list += [file for file in path_list if date in file]
    return file_list


def get_file_list_by_month_range(path, begin, end):
    file_list = []
    path_list = glob(path + '/*')
    dates = month_range(begin, end)
    for date in dates:
        file_list += [file for file in path_list if date in file]
    return file_list


def load_files_content(path, begin, end, columns):
    file_list = get_file_list_by_date_range(path, begin, end)
    content = pd.DataFrame()
    for file in file_list:
        df = pd.read_csv(file, header=[0, 1], ignore_index=True, names=columns, comment='#')
        content = content.append(df)
    return content


def date_str_adjust(date_str, delta=0):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    date += timedelta(delta)
    return datetime.strftime(date, '%Y-%m-%d')


def date_adjust(date_str, delta=0):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    date += timedelta(delta)
    return date


def datetime2unix(date):
    # return np.int64(datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=timezone.utc).timestamp() * 1000)
    return np.int64(parse(date).replace(tzinfo=timezone.utc).timestamp() * 1000)


def unix2datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
