import requests
import pandas as pd
import datetime
from datetime import timedelta, datetime


token = "$API_KEY"

SP = pd.read_csv(r"/mnt/d/Projects/Me/tilingo-gcf-bq/SP_stocks.csv")

ticker_symbols = list(SP["Symbol"])
ticker_symbols.append("SPY")
end_date = str(datetime.now().date()-timedelta(days=1))
