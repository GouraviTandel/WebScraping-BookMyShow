import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
driver=webdriver.Chrome(options=chrome_options)
import time


BMS_url="https://in.bookmyshow.com/explore/home"
driver.get(BMS_url)
#time.sleep(10)
cities=driver.find_elements(By.TAG_NAME,'div')
driver.implicitly_wait(30)
print('cities',cities)
df=pd.DataFrame(cities)
#df.to_csv('div_tag.csv')


data=cities.find_element(By.CLASS_NAME,'sc-kaNhvL jlISnX ellipsis')
title=data.text
print('title',title)