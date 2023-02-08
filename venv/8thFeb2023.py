# Web Scrapping Using Selenium and Pandas Without Opening the Browser Automatically

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from _datetime import datetime
import os
import sys

# This is to create exe of this program
application_path = os.path.dirname(sys.executable)

# This is for checking the system date
now = datetime.now()
dt = now.strftime("%m%d%Y")

# This is for NOT OPENING the Chrome Browser
option = Options()
option.headless = True


# provide drivers and executable path of chromedriver and path of website to open
driver_service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=driver_service, options=option)
driver.get('https://www.thesun.co.uk/sport/football/')

# list in which will provide the data by pandas
title_list = []
subtitle_list = []
link_list = []

# Web scrapping using XPATH
containers = driver.find_elements(By.XPATH, value='//div[@class="teaser__copy-container"]')

for container in containers:
    tittle = container.find_element(By.XPATH, value='./a/h3').text
    subtitle = container.find_element(By.XPATH, value='./a/p').text
    link = container.find_element(By.XPATH, value='./a').get_attribute('href')
    title_list.append(tittle)
    subtitle_list.append(subtitle)
    link_list.append(link)

# Dictionary Created to enter Data Using Pandas
dictionary_list = {'Title': title_list, 'Subtitle': subtitle_list, 'Link': link_list}
dataFrame = pd.DataFrame(dictionary_list)

# Using PANDAS Created File news.csv and Enter the data into it
filename = f'NewsWithoutOpenBrowser_{dt}.csv'
finalPath = os.path.join(application_path, filename)
dataFrame.to_csv(finalPath)

# This is to terminate the browser
driver.quit()
