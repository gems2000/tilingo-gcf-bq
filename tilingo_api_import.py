import requests
import pandas as pd
import datetime
from datetime import timedelta, datetime
from dotenv import load_dotenv
import os


token = os.environ.get('API_KEY')

SP = pd.read_csv(r"/mnt/d/Projects/Me/tilingo-gcf-bq/SP_stocks.csv")

ticker_symbols = list(SP["Symbol"])
ticker_symbols.append("SPY")
end_date = str(datetime.now().date()-timedelta(days=1))


data1 = []

for symbol in ticker_symbols:
    #rate limiter breakpoint
    try:
        url = "https://api.tiingo.com/tiingo/daily/<ticker>/prices?startDate=2019-1-1&endDate=2021-1-1".format(symbol,end_date, token)

        r = requests.get(url, timeout=10)
        rows = r.text.split("\n")[1:-1]
        df = pd.DataFrame(rows)

        df = df.iloc[:,0].str.split(",",13,expand=True)

        df["Symbol"] = symbol
        data1.append(df)
    
    except:
        break


df_final = pd.concat(data1)
df_final.drop(df_final.iloc[:,6:13], axis=1, inplace=True)
df_final.to_csv(r"/mnt/d/Projects/Me/tilingo-gcf-bq/historicalSP.csv", index=False)
