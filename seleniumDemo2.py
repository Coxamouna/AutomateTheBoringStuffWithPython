from selenium import webdriver
import pyinputplus as pyip

browser = webdriver.Firefox()
browser.get("https://github.com/login")
userElem = browser.find_element_by_id("login_field")
userUser = pyip.inputStr("Enter your username: ")
userElem.send_keys(userUser)
passwordElem = browser.find_element_by_id("password")
userPassword = pyip.inputPassword("Enter your password: ")
passwordElem.send_keys(userPassword)
passwordElem.submit()