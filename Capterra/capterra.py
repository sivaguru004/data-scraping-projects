from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

detail = {'name':[], 'review':[]}

a = input('enter the company name: ')
s = a.replace(" ","%20")

driver = webdriver.Firefox()
driver.get(f"https://www.capterra.com/search/?search={s}")
sleep(3)

element = driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "nb-justify-center", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "nb-button-secondary", " " ))]')
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - window.innerHeight/2);",element)
sleep(3)
print('done')

element.click()
sleep(20)

for i in range(1,51):
    try:
        na= driver.find_element(By.XPATH,f'/html/body/div[1]/div/div[2]/div/div[4]/div/div[3]/div[{i}]/div/div/div[1]/div[1]/div/div[1]').text
        detail['name'].append(na)
    except:
        na = driver.find_element(By.XPATH,f'/html/body/div[1]/div/div[2]/div/div[4]/div/div[3]/div[{i}]/div/div/div[1]/div[1]/div[2]/div[1]').text
        detail['name'].append(na)

    
    orl = driver.find_element(By.XPATH,f'/html/body/div[1]/div/div[2]/div/div[4]/div/div[3]/div[{i}]/div/div/div[2]/div[1]').text
    detail['review'].append(orl)
    
print(detail)

df = pd.DataFrame.from_dict(detail, orient='index')
df = df.transpose()

df.to_excel(r'C:\Users\HP\Desktop\intern\excel\capterra.xlsx',index=False)