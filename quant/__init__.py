import json
import os
import time

from loguru import logger

__version__ = "0.0.1"

ROOT_DIR = os.path.abspath('.')
CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))


def init_log():

    log_path = g_config['LOG_PATH']

    if not os.path.exists(log_path):
        os.mkdir(log_path)

    LOG_FILE = os.path.join(log_path, time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log')

    logger.add(LOG_FILE,
               format="{time:YYYY-MM-DD HH:mm:ss} {level} {function} {thread}: {message}",
               level='DEBUG',
               encoding='utf-8',
               rotation="1 day",
               retention='30 days')


def config_load(config_file) -> dict:
    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise FileNotFoundError(f'cannot find config file: {config_file}')


def init_config() -> dict:
    config_file = os.path.join(CONFIG_PATH, 'config.json')
    return config_load(config_file)


g_config = init_config()

init_log()
