from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

search = input("search here:").replace(' ','%20')
detail = {"name":[], "Profile_URL":[]}
url = f"https://www.linkedin.com/search/results/people/?keywords={search}&origin=CLUSTER_EXPANSION&sid=gHm"

driv = r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driv)
driver.get(url)

signin = driver.find_element('xpath','/html/body/div[1]/main/p[1]/a').click()
sleep(2)
E_mail = driver.find_element('xpath','//*[@id="username"]').send_keys('Email')
sleep(3)
pass_word = driver.find_element('xpath','//*[@id="password"]').send_keys('password')
sleep(2)
logIn = driver.find_element('xpath','//*[@id="organic-div"]/form/div[3]/button').click()
sleep(7)

soup = BeautifulSoup(driver.page_source,'html.parser')

ac = soup.find_all('li',class_="reusable-search__result-container")

for i in ac:
    name = i.find('span',dir="ltr").find('span').text
    detail['name'].append(name)
    link = i.find('a',class_="app-aware-link scale-down").get('href')
    detail['Profile_URL'].append(link)
  
df = pd.DataFrame(detail)
print(pd)

df.to_excel(r'C:\Users\HP\Desktop\intern\excel\linkedIn.xlsx',index=False)

driver.close()