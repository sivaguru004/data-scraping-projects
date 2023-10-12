from selenium import webdriver
import pandas as pd
from time import sleep


url = r"https://www.facebook.com/groups/5857109064338371/members"
driv = r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driv)
driver.get(url)

sleep(2)
email = driver.find_element('xpath','//*[@id="email"]').send_keys('sivagurum004@gmail.com')
sleep(4)
pwd = driver.find_element('xpath','//*[@id="pass"]').send_keys('Sivaguru123@')
sleep(5)
login = driver.find_element('xpath','//*[@id="loginbutton"]').click()
sleep(5)

df = pd.read_excel('friend profile excel')
urls = list(df.fb_link)

for i in urls:
    driver.get(i)
    sleep(2)
    f = driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "xtk6v10", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "xuxw1ft", " " ))]')
    
    aa = driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "xtk6v10", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "xuxw1ft", " " ))]').text
    
    if aa == "Add friend":
        msg = driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "xusnbm3", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "x1ye3gou", " " )) and contains(concat( " ", @class, " " ), concat( " ", "x1qhmfi1", " " ))]').click()
    else:
        driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "xtvsq51", " " ))]').click()
    sleep(10)
    
    a = driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "x2b8uid", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "xuxw1ft", " " ))]').text

    msg = driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "x1odjw0f", " " )) and contains(concat( " ", @class, " " ), concat( " ", "notranslate", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "xdj266r", " " ))]').send_keys('hi ',a)
    sleep(2)
    
    send = driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "xw3qccf", " " )) and contains(concat( " ", @class, " " ), concat( " ", "xurb0ha", " " ))]').click()
    sleep(2)
    
    driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "x1qrby5j", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "x1a2a7pz", " " ))]').click()
    sleep(2)