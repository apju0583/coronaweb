from django.shortcuts import render
from django.http import HttpResponse
import csv
import pandas as pd
import requests, io

# Create your views here.
def index(request) :
    from polls.models import World_daily

    url='https://raw.githubusercontent.com/microsoft/Bing-COVID-19-Data/146151c99d24a60a6c53d8a80e53cdaf8a03856c/data/Bing-COVID19-Data.csv'
    c=requests.get(url).content
    s=pd.read_csv(io.StringIO(c.decode('utf-8')))

    for data in s.values:
        p=World_daily(world_date=data[1], world_confirmed=data[2], world_confirmed_change=data[3], world_death=data[4], world_death_change=data[5], world_country=data[12])
        p.save()

 
