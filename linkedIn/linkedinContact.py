from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

detail = {"name":[], "profile_URL":[], "Number":[], "mail":[]}
url = r"https://www.linkedin.com/mynetwork/invite-connect/connections/"

driv = r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driv)
driver.get(url)
sleep(5)
signin = driver.find_element('xpath','/html/body/div[1]/main/p[1]/a').click()
sleep(7)
E_mail = driver.find_element('xpath','//*[@id="username"]').send_keys('Email')
sleep(5)
pass_word = driver.find_element('xpath','//*[@id="password"]').send_keys('password')
sleep(2)
logIn = driver.find_element('xpath','//*[@id="organic-div"]/form/div[3]/button').click()
sleep(4)

soup = BeautifulSoup(driver.page_source,'html.parser')
act = soup.find_all('li',class_="mn-connection-card artdeco-list")

for ac in act:
    profile = ac.find('a', class_='ember-view mn-connection-card__picture').get('href')
    link = 'https://www.linkedin.com/'+profile
    detail['profile_URL'].append(link)
    name = ac.find('span', class_ ="mn-connection-card__name t-16 t-black t-bold").text
    detail['name'].append(name)
    sleep(1)
    info = link +"overlay/contact-info/"
    driver.get(info)
    sleep(1)
    contact = BeautifulSoup(driver.page_source,'html.parser')
    try:
        number = contact.find('ul',class_="list-style-none").find('span', class_="t-14 t-black t-normal").text
        detail['Number'].append(number)
    except:
        detail['Number'].append('No Number')
    try:
        mail = contact.find('section',class_="pv-contact-info__contact-type ci-email").find('div', class_="pv-contact-info__ci-container t-14").a.text
        detail['mail'].append(mail)
    except:
        detail['mail'].append('No Email')
    
df = pd.DataFrame(detail)
print(df)

df.to_excel(r'C:\Users\HP\Desktop\intern\excel\linkedIn_contact2.xlsx',index=False)

driver.close()