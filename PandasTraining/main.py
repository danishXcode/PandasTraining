# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import talib.abstract as ta
import qtpylib.indicators as qtpylib


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    filename = "ETH_USDT-15m.csv"
    df = pd.read_csv(filename)
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    df.date = pd.to_datetime(df['date'], unit='ms')
    df = df.loc[df['date'] > (datetime.now() - timedelta(days=7))]
    bollinger = qtpylib.bollinger_bands(qtpylib.typical_price(df), window=20, stds=2)
    df["bb_lower"] = bollinger['lower']
    df["bb_mid"] = bollinger['mid']
    df["rsi"] = ta.RSI(df)
    df.loc[
        (qtpylib.crossed_below(df["close"], df["bb_lower"])) & (df["rsi"] < 30)
        , 'buy'] = 1
    df.loc[
        (qtpylib.crossed_above(df["close"], df['bb_mid']))
        & (df["rsi"] > 30), "sell"
    ] = 1

    print("rsi")
    print(df.loc[(df["buy"] == 1) | (df["sell"] == 1)])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
