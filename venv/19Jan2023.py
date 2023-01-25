import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://quotes.toscrape.com/')

driver.find_element(By.CSS_SELECTOR, 'div.col-md-4 p a').click()

username = driver.find_element(By.CSS_SELECTOR, 'input#username')
username.send_keys('abcd')

password = driver.find_element(By.CSS_SELECTOR, 'input#password')
password.send_keys('abcd')

driver.find_element(By.CSS_SELECTOR, 'input.btn').click()

# First Page
for div in driver.find_elements(By.CSS_SELECTOR, 'div.quote'):
    print("{0} - {1}".format(div.find_element(By.CSS_SELECTOR, 'span.text').text, div.find_element(By.CSS_SELECTOR,
                                                                                                   'small.author')
                             .text))

# Next Page - 2
driver.find_element(By.CSS_SELECTOR, 'li.next a').click()
for div in driver.find_elements(By.CSS_SELECTOR, 'div.quote'):
    print("{0} - {1}".format(div.find_element(By.CSS_SELECTOR, 'span.text').text, div.find_element(By.CSS_SELECTOR,
                                                                                                   'small.author')
                             .text))

# Next Page - 3
driver.find_element(By.CSS_SELECTOR, 'li.next a').click()
for div in driver.find_elements(By.CSS_SELECTOR, 'div.quote'):
    print("{0} - {1}".format(div.find_element(By.CSS_SELECTOR, 'span.text').text, div.find_element(By.CSS_SELECTOR,
                                                                                                   'small.author')
                             .text))
