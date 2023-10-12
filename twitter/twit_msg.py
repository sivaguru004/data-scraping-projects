from selenium import webdriver
import pandas as pd
from time import sleep

url = r'https://twitter.com/i/flow/login'
driv = r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driv)
driver.get(url)
sleep(3)

driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div').click()
sleep(3)
driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys('user name')
sleep(4)
driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
sleep(3)
driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys('password')
sleep(4)
driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
sleep(5)

df = pd.read_excel(r'C:\Users\HP\Desktop\intern\excel\twit_url.xlsx')
urls = list(df.link)

for i in urls:
    driver.get(i)
    sleep(4)
    driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div').click()
    sleep(3)
    driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "public-DraftStyleDefault-ltr", " " ))]').click()
    sleep(2)
    driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "public-DraftStyleDefault-ltr", " " ))]').send_keys('hi')
    sleep(3)
    driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "r-13hce6t", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "r-q4m81j", " " ))]').click()
    sleep(3)