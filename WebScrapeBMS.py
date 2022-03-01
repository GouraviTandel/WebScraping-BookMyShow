import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BMS_url="https://in.bookmyshow.com/explore/home"
response=requests.get(BMS_url)
response.status_code
with open("BMS.html","w") as f:
    f.write(response.text)

with open('BMS.html','r') as file:
    html_source=file.read()
BMS_doc=BeautifulSoup(html_source,'html.parser')

Title=BMS_doc.title
Cities=BMS_doc.find_all(class_="sc-iuDHTM uqCMs")
print('Cities',Cities)
