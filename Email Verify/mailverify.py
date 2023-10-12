from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

gmail = input('enter your mail:')

url = r"https://email-checker.net/validate"
driv = r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driv)
driver.get(url)

sleep(3)
email = driver.find_element('xpath','//*[@id="ltrInput"]').send_keys(gmail)
sleep(5)

check = driver.find_element('xpath','//*[@id="mainForm"]/div[2]/button').click()

soup = BeautifulSoup(driver.page_source,'html.parser')

verify = soup.find('div',class_ = 'info').p.em.text
print(verify)