import csv
import pandas as pd
import requests
import io

url='https://raw.githubusercontent.com/microsoft/Bing-COVID-19-Data/146151c99d24a60a6c53d8a80e53cdaf8a03856c/data/Bing-COVID19-Data.csv'
c=requests.get(url).content
s=pd.read_csv(io.StringIO(c.decode('utf-8')))

print(s)
