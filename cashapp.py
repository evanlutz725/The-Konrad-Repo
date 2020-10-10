#!/usr/bin/python
# Send a dollar from your account to another with Cashapp
# NOTE: Executable for Linux
# NOTE: All PII values have been starred out
# TODO: Loop through and do 10 $1 transactions and then request $10
# TODO: use Tkinter for GUI input
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox()
driver.get('https://cash.app/login')
sleep(5)
elem = driver.find_element_by_name("alias")
elem.send_keys('**********') #phone number
elem.send_keys(Keys.ENTER)
sleep(5)
elem = driver.find_element_by_name("code")
x = raw_input('Enter code: ') # sms text login code
elem.send_keys(x)
elem.send_keys(Keys.ENTER)
sleep(5)
elem = driver.find_element_by_name("pan")
elem.send_keys('****************') # credit card number
elem.send_keys(Keys.ENTER)
sleep(5)
driver.find_element_by_class_name('create-payment')
button = driver.find_element_by_class_name('create-payment')
button.click()
sleep(5)
button = driver.find_element_by_class_name('live-input')
button.send_keys('$**********') # account to send a dollar to
button = driver.find_element_by_class_name('whole-amount-value')
button.send_keys('1')
button = driver.find_element_by_class_name('request')
x = raw_input('press enter to send a dollar:')
button.click()


