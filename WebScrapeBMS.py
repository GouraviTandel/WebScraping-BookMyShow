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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BMS_url="https://in.bookmyshow.com/explore/home"
driver.get(BMS_url)
#time.sleep(10)
#cities=driver.find_elements(By.TAG_NAME,'div')
driver.implicitly_wait(30)
#WebDriverWait(driver, 10);
#print('cities',cities)
#df=pd.DataFrame(cities)
#df.to_csv('div_tag.csv')

#WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,"sc-jKVCRD hmbjRr")))
driverdata=driver.find_element_by_class_name('sc-kaNhvL.jlISnX.ellipsis')
#title=data
print(driverdata.text)