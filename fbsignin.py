




from selenium import webdriver as sw
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

service = Service('D:\\Selenium Project\\chromedriver_win32\\chromedriver.exe')
service.start()
driver = sw.Remote(service.service_url)
driver.get('https://www.facebook.com/');

ca=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a")
ca.click()
time.sleep(10)

fname=driver.find_element_by_name('firstname')
fname.send_keys("tanishka")

lname=driver.find_element_by_name('lastname')
lname.send_keys("joshi")

email=driver.find_element_by_name('reg_email__')
email.send_keys("tanishkaj495@gmail.com")

cemail=driver.find_element_by_name('reg_email_confirmation__')
cemail.send_keys("tanishkaj495@gmail.com")

password=driver.find_element_by_name('reg_passwd__')
password.send_keys("t@nuJoshi4")


days = driver.find_element_by_id('day')
drop = Select(days)
drop.select_by_visible_text("4")

months= driver.find_element_by_id('month')
drop = Select(months)
drop.select_by_visible_text("12")

years= driver.find_element_by_id('year')
drop = Select(years)
drop.select_by_visible_text("1995")

gender=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input")
gender.click()


signin=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[10]/button")
signin.click()
time.sleep(10)




