from pycoingecko import CoinGeckoAPI
from pandas import DataFrame as df
import pandas as pd
import numpy as np

pd.set_option('float_format', '{:f}'.format)
def getCurrency(name):
    cg = CoinGeckoAPI()
    data = cg.get_coins_markets(vs_currency='usd', ids=name, order='market_cap_desc', per_page='100', page='1',
                                price_change_percentage='1h')
    return data[0]


def getALL():
    currency = ['bitcoin', 'ethereum','eos','eos',
                'litecoin', 'bitcoin-cash', 'tether', 'stellar', 'tron', 'binancecoin', 'bitcoin-cash-sv', 'cardano',
                'monero', 'iota', 'dash', 'maker', 'neo', 'ethereum-classic', 'nem']
    allcoins = []

    for coin in currency:
        result = getCurrency(coin)

        allcoins.append(result)
        allcoins.sort(key=lambda c: c['market_cap_rank'])
        allcoins=allcoins[:15]

    df2 = df(allcoins, columns=['name', 'market_cap'])

    #newlist = []



    return df2

def Volume():
    currency = ['bitcoin', 'ethereum', 'eos', 'eos',
                'litecoin', 'bitcoin-cash', 'tether', 'stellar', 'tron', 'binancecoin', 'bitcoin-cash-sv', 'cardano',
                'monero', 'iota', 'dash', 'maker', 'neo', 'ethereum-classic', 'nem']
    allcoins = []

    for coin in currency:
        result = getCurrency(coin)

        allcoins.append(result)
        allcoins.sort(key=lambda c: c['market_cap_rank'])
        allcoins = allcoins[:15]

    totalvolume = df(allcoins, columns=['name', 'total_volume'])

    return totalvolume

def MarketCapChange():
    currency = ['bitcoin', 'ethereum', 'eos', 'eos',
                'litecoin', 'bitcoin-cash', 'tether', 'stellar', 'tron', 'binancecoin', 'bitcoin-cash-sv', 'cardano',
                'monero', 'iota', 'dash', 'maker', 'neo', 'ethereum-classic', 'nem']
    allcoins = []

    for coin in currency:
        result = getCurrency(coin)

        allcoins.append(result)
        allcoins.sort(key=lambda c: c['market_cap_rank'])
        allcoins = allcoins[:15]

    total24change = df(allcoins, columns=['name', 'market_cap_change_percentage_24h'])

    return total24change



