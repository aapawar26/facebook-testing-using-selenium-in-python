from selenium import webdriver
import time

email = input("Enter email : ")
password = input("Enter Password : ")


driver = webdriver.Chrome()
driver.get('https://facebook.com')

em = driver.find_element_by_xpath('//input[@name ="email"]')
em.send_keys(email)

ps = driver.find_element_by_xpath('//input[@name ="pass"]')
ps.send_keys(password)

login = driver.find_element_by_id('loginbutton')
login.click()


time.sleep(5)
