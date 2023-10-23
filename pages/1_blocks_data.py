import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import statsmodels.api as sm

st.markdown("# Blocks data")
st.sidebar.markdown("# Blocks data")

left_column, right_column = st.columns(2)

st.cache_data()
def open_blocks_data():
    df_blockstats_daily_mean = pd.read_csv('/home/moises/Data_BTC_thesis/df_blockstats_daily_mean.csv')
    for col in df_blockstats_daily_mean.columns:
        #transformar em float
        try:
            df_blockstats_daily_mean[col] = df_blockstats_daily_mean[col].astype(float)
        except:
            print(col)
            pass
         
    df_blockstats_daily_mean["GMT"] = pd.to_datetime(df_blockstats_daily_mean["GMT"])
    df_blockstats_daily_mean["Date"] = pd.to_datetime(df_blockstats_daily_mean["Date"])
    df_blockstats_daily_mean.set_index("GMT", inplace=True)
    return df_blockstats_daily_mean
df_blockstats_daily_mean = open_blocks_data()

st.cache_data()
def open_prices_data():
    # Main resource of bitcoin price is the data from ccxt 
    #import df_price_btc_usd_agregate.csv
    df_price_btc_usd_agregate = pd.read_csv("/home/moises/Data_BTC_thesis/df_price_btc_usd_agregate.csv")
    #convert the Date column to datetime
    df_price_btc_usd_agregate["Date"] = pd.to_datetime(df_price_btc_usd_agregate["Date"])
    #set the Date column as index
    #df_price_btc_usd_agregate.set_index("Date", inplace=True)
    btc_price_data = df_price_btc_usd_agregate 
    btc_price_data["Close"] = btc_price_data["Close"].astype(float)
    #set the Date column as index
    btc_price_data.set_index("Date", inplace=True)

    return btc_price_data
btc_price_data = open_prices_data()

dict_col_names = {col:{"log":True, "ylabel":True } for col in df_blockstats_daily_mean.columns} 
dict_col_names["avgfee"] = {"log":True, "ylabel":"sats"}
dict_col_names["avgfeerate"] = {"log":True, "ylabel":"sats/vbyte"}
dict_col_names["avgtxsize"] = {"log":True, "ylabel":"bytes"}
dict_col_names["blockhash"] = {"log":True, "ylabel":None}
dict_col_names["feerate_percentiles"] = {"log":True, "ylabel":None}
dict_col_names["height"] = {"log":True, "ylabel":None}
dict_col_names["ins"] = {"log":False, "ylabel":None}
dict_col_names["maxfee"] = {"log":True, "ylabel":"sats"}
dict_col_names["maxfeerate"] = {"log":True, "ylabel":"sats/vbyte"}
dict_col_names["maxtxsize"] = {"log":False, "ylabel":"bytes"}
dict_col_names["medianfee"] = {"log":True, "ylabel":"sats"}
dict_col_names["mediantime"] = {"log":True, "ylabel":None}
dict_col_names["mediantxsize"] = {"log":True, "ylabel":"bytes"}    
dict_col_names["minfee"] = {"log":True, "ylabel":"sats"}
dict_col_names["minfeerate"] = {"log":True, "ylabel":"sats/vbyte"}
dict_col_names["mintxsize"] = {"log":True, "ylabel":"bytes"}
dict_col_names["outs"] = {"log":False, "ylabel":None}
dict_col_names["subsidy"] = {"log":True, "ylabel":"sats"}
dict_col_names["swtotal_size"] = {"log":False, "ylabel":"bytes"}
dict_col_names["swtotal_weight"] = {"log":False, "ylabel":"wu"}
dict_col_names["swtxs"] = {"log":False, "ylabel":None}
dict_col_names["time"] = {"log":True, "ylabel":None}
dict_col_names["total_out"] = {"log":True, "ylabel":"sats"}
dict_col_names["total_size"] = {"log":False, "ylabel":"bytes"}
dict_col_names["total_weight"] = {"log":False, "ylabel":"wu"}
dict_col_names["totalfee"] = {"log":True, "ylabel":"sats"}
dict_col_names["txs"] = {"log":False, "ylabel":None}
dict_col_names["utxo_increase"] = {"log":False, "ylabel":None}
dict_col_names["utxo_size_inc"] = {"log":False, "ylabel":None}
dict_col_names["utxo_size_inc_actual"] = {"log":False, "ylabel":None}
dict_col_names["GMT"] = {"log":True, "ylabel":None}
dict_col_names["year"] = {"log":True, "ylabel":None}
dict_col_names["avgfee_btc"] = {"log":True, "ylabel":"BTC"}
dict_col_names["maxfee_btc"] = {"log":True, "ylabel":"BTC"}
dict_col_names["minfee_btc"] = {"log":True, "ylabel":"BTC"}
dict_col_names["subsidy_btc"] = {"log":True, "ylabel":"BTC"}
dict_col_names["blockhash_decimal"] = {"log":True, "ylabel":None}


list_fee_names = ["avgfee", "avgfeerate", "maxfee", "maxfeerate", "medianfee", "minfee", "minfeerate", "totalfee"]
list_size_names = ["avgtxsize", "maxtxsize", "mediantxsize", "mintxsize", "swtotal_size", "swtotal_weight", "total_size", "total_weight"]
list_count_names = ["ins", "outs", "swtxs", "txs", "utxo_increase", "utxo_size_inc", "utxo_size_inc_actual"]
list_time_names = ["time", "mediantime"]
list_subsidy_names = ["subsidy", "subsidy_btc"]
list_block_names = ["blockhash", "blockhash_decimal", "height", "year", "GMT"]
list_other_names = ["feerate_percentiles"]
 


#df_blockstats_daily_mean

left_column.markdown("## Fees")

#plot the fees in scatterplot
option_type_of_features = left_column.selectbox(
    "Which type of feature do you want to see?",
    ["Fees", "Size", "Count", "Time", "Subsidy", "Block", "Other"]
)

if option_type_of_features == "Fees":
    list_features = list_fee_names
elif option_type_of_features == "Size":
    list_features = list_size_names
elif option_type_of_features == "Count":
    list_features = list_count_names
elif option_type_of_features == "Time":
    list_features = list_time_names
elif option_type_of_features == "Subsidy":
    list_features = list_subsidy_names
elif option_type_of_features == "Block":
    list_features = list_block_names
elif option_type_of_features == "Other":
    list_features = list_other_names

option_column = left_column.selectbox(
    "Select your feature",
    list_features
)
left_column.line_chart(df_blockstats_daily_mean[option_column])
right_column.markdown("## Price")
right_column.write(" ")
right_column.write(" ")
right_column.write(" ")
right_column.write(" ")
right_column.write(" ")
right_column.line_chart(btc_price_data["Close"])


left_column.markdown("## CCF")
left_column.write("Cross Correlation Function (lags in price)")
#plot the cross correlation between fees and price 

ccf_lags_values = sm.tsa.stattools.ccf(btc_price_data["Close"],df_blockstats_daily_mean[option_column], adjusted=False)

left_column.bar_chart(ccf_lags_values)

right_column.write(f"Cross Correlation Function (lags in {option_column})")
#plot the cross correlation between fees and price 

ccf_lags_values_2 = sm.tsa.stattools.ccf(df_blockstats_daily_mean[option_column],btc_price_data["Close"], adjusted=False)


right_column.bar_chart(ccf_lags_values_2)