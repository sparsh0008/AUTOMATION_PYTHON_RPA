# Open Browser In The New Tab Whatsapp to send the message
import pywhatkit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Below code is used to send Message on whatsapp automatically by using pywhatkit
# Enter Phone Number
# phone1 = input("Enter the contact Number : ")
# PhoneNumber1 = "+91" + phone1
# print(PhoneNumber1)
# pywhatkit.sendwhatmsg(PhoneNumber1, "Automation Testing", 12, 24)

# Below code is used to send Message on whatsapp automatically by using Selenium module
phone = input("Enter the contact Number : ")
PhoneNumber = "+91" + phone
mess = input("What Message You Want to send : ")

WhatsappWeb = "https://web.whatsapp.com/"
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get(WhatsappWeb)
time.sleep(20)

# Search the Contact Number and Click the Contact to send the message
searchContact = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
searchContact.send_keys(PhoneNumber, Keys.ENTER)
time.sleep(5)

# Enter the Message You want to send to that Person
messageBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
messageBox.send_keys(mess, Keys.ENTER)
time.sleep(5)

print("Message {1} is send to {0} ".format(PhoneNumber, mess))

