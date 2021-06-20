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

