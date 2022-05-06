import json
import urllib.request


def get_all_symbols():
    response = urllib.request.urlopen("https://api.binance.com/api/v3/exchangeInfo").read()
    return list(map(lambda symbol: symbol['symbol'], json.loads(response)['symbols']))

def get_future_cm():