from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import seaborn as sns
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  
from functools import lru_cache
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("moises", "moises123"),timeout=100000)


def insert_price_btc_in_df_blockstats_daily(df_blockstats_daily, btc_price_data): 
    df_blockstats_daily["GMT"] = pd.to_datetime(df_blockstats_daily["time"], unit="s")
    df_blockstats_daily["GMT"] =df_blockstats_daily["GMT"].dt.date
    df_blockstats_daily["GMT"] 

    btc_price_data['Date'] = pd.to_datetime(btc_price_data['Date'])
    btc_price_data['Date'] = btc_price_data['Date'].dt.date
    btc_price_data["Close"]

    # merge the btc_price_data["Close"] with the date to the df_blockstats_daily dataframe on the column GMT
    df_blockstats_daily = df_blockstats_daily.merge(btc_price_data[["numeric_date", "Close", "Date"]], left_on="GMT", right_on="Date", how="left")
    return df_blockstats_daily

