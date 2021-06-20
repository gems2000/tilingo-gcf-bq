import requests
import pandas as pd
from bs4 import BeautifulSoup

#import url
url = ""


#cache requests
r = requests.get(url, timeout=3)
r_html = r.text

#tag retreival from html
soup = BeautifulSoup(r_html, 'html.parser')
components_table = soup.find_all(id="constituents")


#store in pandas
headers = soup.find_all("th")
df_columns = [item.text.rstrip("\n") for item in headers]
comp_headers = df_columns[:9]
data_row = components_table[0].find("tbody").find_all("tr")[1:]

rows =[]
for row in range(data_row):
    stocks = list(filter(None,data_row[row].text.split("\n")))
    rows.append(stocks)

S_P_stocks = pd.DataFrame(rows, columns=comp_headers)


#save dataset into csv
S_P_stocks.drop("SEC Fill", inplace=True, axis=1)
S_P_stocks.to_csv(r"/mnt/d/Projects/Me/tilingo-gcf-bq/SP_stocks.csv", index=False)

