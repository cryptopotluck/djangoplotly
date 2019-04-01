from binance.client import Client

from datetime import datetime
from .keys import APIKey, SecretKey

from pandas import DataFrame as df

client = Client(api_key=APIKey, api_secret=SecretKey)
def create_coin_dataframe():
    #Call on API for Data
    candles = client.get_klines(symbol='LTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR)
    #put data in a dataframe
    candles_data_frame2 = df(candles)

    #Parse dataframe for only the date in milliseconds
    candles_data_frame = candles_data_frame2[0]

    #create empty list
    finaldate = []

    #create a loop for each date
    for time2 in candles_data_frame.unique():
        #turn date into something thats actually readable
        readable = datetime.fromtimestamp(int(time2/1000))
        #add date to empty list
        finaldate.append(readable)



    #candles=(candles[0][0]/1000)
    #readable = datetime.fromtimestamp(int(candles))

    #call on origional list & remove junk
    candles_data_frame2.pop(0)
    candles_data_frame2.pop(11)

    #put the new dates in a dataframe
    datedataframe = df(finaldate)


    #rename date dataframe to have column date
    datedataframe.columns = ['date']
    #bring the two dataframes together
    finaldataframe= datedataframe.join(candles_data_frame2)
    #set date column as the index
    finaldataframe.set_index('date', inplace=True)
    #rename the blank columns to match what they represent
    finaldataframe.columns = ['open', 'high', 'low', 'close', 'volume', 'close_time', 'asset_volume', 'trade_number', 'taker_buy_base', 'taker_buy_quote']
    #finaldataframe['date'] = pd.to_datetime(finaldataframe['date'])
    return finaldataframe

