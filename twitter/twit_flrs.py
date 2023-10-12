from selenium import webdriver
import pandas as pd
from time import sleep

detail = {'name':[], 'id':[], 'profile_url':[], 'profile_img':[], 'discription':[]}

url = r'https://twitter.com/i/flow/login'
dri = r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(dri)
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


driver.get('https://twitter.com/SakthiSharma17/followers')
sleep(5)
for  i in range(1,999):
    try:
        nam = driver.find_element('xpath',f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div/div[1]/div/div[1]/a/div/div[1]/span/span[1]')
        # print(nam.text)
        detail['name'].append(nam.text)
        ida = driver.find_element('xpath',f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/a/div/div/span').text
        ids = ida.replace('@','')
        detail['id'].append(ids)
        # print(ids)
        profil = 'https://twitter.com/'+ids
        # print(profil)
        detail['profile_url'].append(profil)
        img = profil + '/photo'
        # print(img)
        detail['profile_img'].append(img)
        try:
            dis = driver.find_element('xpath',f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[2]/span').text
            # print(dis) 
            detail['discription'].append(dis)
        except:
            # print('no discription')
            detail['discription'].append('no discription') 
    except:
        break

# driver.get(profil)
# sleep(5)
# fling =driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "r-1mf7evn", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "r-b88u0q", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "r-qvutc0", " " ))]').text
# print('following:',fling)
# flrs = driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div[2]/div[4]/div[2]/a/span[1]/span').text
# print('followers:',flrs)

df = pd.DataFrame(detail)
print(df)

df.to_excel(r'C:\Users\HP\Desktop\intern\excel\twitter_followers2.xlsx',index=False)