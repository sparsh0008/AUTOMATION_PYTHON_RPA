# Open Browser In The New Tab Whatsapp to send the message

import pywhatkit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# # Enter Phone Number
# phone1 = input("Enter the contact Number : ")
# PhoneNumber1 = "+91" + phone1
# print(PhoneNumber1)
# pywhatkit.sendwhatmsg(PhoneNumber1, "Automation Testing", 12, 24)

# Upper code is used to send Message on whatsapp automatically by using pywhatkit module but now the same should be done
# by selenium

phone = input("Enter the contact Number : ")
PhoneNumber = "+91" + phone
MessageToSend = "Good Morning today is %A"

WhatsappWeb = "https://web.whatsapp.com/"
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get(WhatsappWeb)
time.sleep(60)

# Search the Contact Number
searchContact = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
searchContact.send_keys(PhoneNumber)
time.sleep(10)

# # Click the Contact to send the message
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[4]/div/div/div').click()
# time.sleep(10)

# # Enter the Message You want to send to that Person
# messageBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
# messageBox.send_keys(MessageToSend)
# time.sleep(15)

# # Click the send Button to send the message
# driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

print("Message {1} is send to {0} ".format(PhoneNumber, MessageToSend))

