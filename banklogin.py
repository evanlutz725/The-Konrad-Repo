#!/usr/bin/python
# Logs into lmcu.com
# Username and Password starred
# Executes on linux
# TODO: Use Tkinter for GUI input
# TODO: Create function to handle captcha inputs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox()
driver.get('https://lmcu.org/')
sleep(2)
# Uncomment below if using webdriver.Chrome()
# driver.maximize_window()
sleep(2)
button = driver.find_element_by_class_name('button-online-banking')
button.click()
sleep(2)
elem = driver.find_element_by_id("UserName")
elem.send_keys('*********')
elem.send_keys(Keys.ENTER)
sleep(5)
elem = driver.find_element_by_name("Password")
elem.send_keys('********')
elem.send_keys(Keys.ENTER)
sleep(5)
elem = driver.find_element_by_link_text('Log Out')
elem.click()
