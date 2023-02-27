# IMPORT LIBS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
import pandas as pd

# THIS IS FOR OPEING THE CHROME BROWSER
driver = webdriver.Chrome()
url = "https://www.cleartrip.com/"
driver.get(url)
driver.maximize_window()

# CLICK THE AREA TO SELECT DESTINATION
source = driver.find_element(By.XPATH,
                             value='//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div['
                                   '3]/div/div/div[1]/input')
source.send_keys("Bangalore")
time.sleep(5)  # HOLD FOR 5 SEC

# CLCIK THE OPTION FROM THE DROP-DOWN
driver.find_element(By.XPATH,
                    value='//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div[1]/div['
                          '1]/div[2]/ul/li/div/div[2]/p').click()
time.sleep(5)  # HOLD FOR 5 SEC

# CLICK THE AREA TO SELECT DESTINATION
destination = driver.find_element(By.XPATH,
                                  value='/html/body/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div['
                                        '3]/div/div/div[3]/input')
destination.send_keys("Delhi")
time.sleep(5)  # HOLD FOR 5 SEC

# CLCIK THE OPTION FROM THE DROP-DOWN
driver.find_element(By.XPATH,
                    value='//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div['
                          '3]/div[3]/div/div[1]/div[3]/div[2]/ul/li/div/div[2]/p').click()
time.sleep(5)  # HOLD FOR 5 SEC

# CLICK THE SEARCH BUTTON
driver.find_element(By.XPATH,
                    value='/html/body/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div['
                          '4]/div/div[2]/span').click()
time.sleep(10)  # HOLD FOR 10 SEC

# THIS IS TO SCROLL DOWN THE PAGE
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)  # HOLD FOR 5 SEC

# SEARCHING ALL THE FLIGHT NAMES IN THE PAGE
flight_name = driver.find_elements(By.XPATH, '//div[@class="flex flex-column flex-start"]')
flight_list = []  # CREATED EMPTY LIST FOR LIST OF AIRLINES
for fn in flight_name:  # FOR LOOP FOR ACCESSING ALL THE FLIGHT DETAILS IN THAT COLOUM
    text_element = fn.find_element(By.XPATH, './/p[@class="fw-500 fs-2 c-neutral-900"]')
    text = text_element.text
    flight_list.append(text)  # APPENDING THE LIST

# SEARCHING ALL THE FLIGHT PRICES IN THE PAGE
price = driver.find_elements(By.XPATH, '//div[@class="flex flex-column flex-center flex-right p-relative"]')
flight_price = []  # CREATED EMPTY LIST FOR FLIGHT PRICES
for fp in price:  # FOR LOOP FOR ACCESSING ALL THE FLIGHT DETAILS IN THAT COLOUM
    text_element = fp.find_element(By.XPATH, './/p[@class="m-0 fs-5 fw-700 c-neutral-900 false"]')
    text = text_element.text.replace("₹", "")
    flight_price.append(text)  # APPENDING THE LIST

# DATAFRAME TO CREATE A LIST
df = pd.DataFrame({"Flight Name": flight_list, "Flight Price": flight_price})
df.to_csv("CA_FLIGHT.csv")  # ENTER DATA TO CSV FLIE

# READ A CSV FILE AND ASSIGN CHEAPEST_PRICE AND CHEAPEST_FLIGHT
df = pd.read_csv('CA_FLIGHT.csv')
cheapest_price = df['Flight Price'].iloc[0]  # THIS WILL READ THE VERY FIRST ROW
cheapest_flight = df['Flight Name'].iloc[0]  # THIS WILL READ THE VERY FIRST ROW

# PRINT CHEAPEST_PRICE AND CHEAPEST_FLIGHT
print(f"The cheapest flight price is {cheapest_price} and cheapest flight name is {cheapest_flight}.")
