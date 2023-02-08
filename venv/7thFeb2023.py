# Web Scrapping Using Selenium and Pandas by Opening the Browser Automatically

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# provide drivers and executable path of chromedriver and path of website to open
driver_service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)
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
dataFrame.to_csv('news.csv')

# This is terminate the browser
driver.quit()
