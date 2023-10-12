from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

detail = {'name':[],'status . members . post':[], 'discription':[], 'group_url':[]}
url = r"https://www.facebook.com/search/groups/?q=food"
driv = r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driv)
driver.get(url)

sleep(2)
email = driver.find_element('xpath','//*[@id="email"]').send_keys('Email')
sleep(4)
pwd = driver.find_element('xpath','//*[@id="pass"]').send_keys('passward')
sleep(5)
login = driver.find_element('xpath','//*[@id="loginbutton"]').click()
sleep(3)

driver.get('https://www.facebook.com/search/groups/?q=food')
sleep(3)

detl = []
for i in range(1,999):
    try:
        nam = driver.find_element('xpath',f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{i}]/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/span/div/a')
        dtl = driver.find_element('xpath',f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{i}]/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/span/span')

        link = driver.find_element('xpath',f'//*[contains(concat( " ", @class, " " ), concat( " ", "x1yztbdb", " " )) and (((count(preceding-sibling::*) + 1) = {i}) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "xzsf02u", " " )) and contains(concat( " ", @class, " " ), concat( " ", "x1s688f", " " ))]').get_attribute('href')
        detail['group_url'].append(link)
        
        try:
            dscrp = driver.find_element('xpath',f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{i}]/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[3]/span/span')
            detail['discription'].append(dscrp.text)
        except:
            detail['discription'].append('no discription')
            
        detail['name'].append(nam.text)
        detail['status . members . post'].append(dtl.text)
    except:
        break        
    
df = pd.DataFrame(detail)
print(df)
