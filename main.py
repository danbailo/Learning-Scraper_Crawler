import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')
if req.status_code == 200:
    print('Requisição bem sucedida!')

print(req.text)