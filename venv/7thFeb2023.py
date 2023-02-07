# Web Scrapping Using Selenium and Pandas

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver_service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)
driver.get('https://www.thesun.co.uk/sport/football/')


title_list = []
subtitle_list = []
link_list = []
containers = driver.find_elements(By.XPATH, value='//div[@class="teaser__copy-container"]')

for container in containers:
    tittle = container.find_element(By.XPATH, value='./a/h3').text
    subtitle = container.find_element(By.XPATH, value='./a/p').text
    link = container.find_element(By.XPATH, value='./a').get_attribute('href')
    title_list.append(tittle)
    subtitle_list.append(subtitle)
    link_list.append(link)

dictionary_list = {'Title': title_list, 'Subtitle': subtitle_list, 'Link': link_list}
dataFrame = pd.DataFrame(dictionary_list)

dataFrame.to_csv('news.csv')
driver.quit()
