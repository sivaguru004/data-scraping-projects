from selenium import webdriver
import pandas as pd
from time import sleep

detail = {'question':[], 'question_url':[], 'upvotes':[]}

url = r"https://www.quora.com/search?q=live%20chat%20tool"

driv = r'C:\Users\HP\Downloads\chromedriver_win32\chramedriver.exe'
browser = webdriver.Chrome(driv)
browser.get(url)

sleep(3)
# t = 0
# last_height = browser.execute_script("return document.body.scrollHeight")
# while True:
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     sleep(1)
#     new_height = browser.execute_script("return document.body.scrollHeight")
#     if new_height < last_height:
#         break
#     elif t == 3:
#         break
#     last_height = new_height
#     t +=1


for i in range(2,99):
    try:
        qus = browser.find_element('xpath',f'//*[@id="mainContent"]/div/div/div[2]/div[{i}]/span/a/div/div/div/div/span').text
        detail['question'].append(qus)
        url = browser.find_element('xpath',f'//*[@id="mainContent"]/div/div/div[2]/div[{i}]/span/a').get_attribute('href')
        detail['question_url'].append(url)
        vote = browser.find_element('xpath',f'//*[@id="mainContent"]/div/div/div[2]/div[{i}]/div/div[1]/div/div[2]/div/div/div/div[2]/div').click()
        sleep(2)
        c = browser.find_element('xpath',f'//*[@id="mainContent"]/div/div/div[2]/div[{i}]/div/div[1]/div/div[3]/div/span/span[4]/div').click()
        sleep(2)
        up = browser.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "qu-bold", " " ))]').text
        detail['upvotes'].append(up)
        x = browser.find_element('xpath','//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/button').click()
    except:
        break

df = pd.DataFrame(detail)
print(df)

df.to_excel(r'C:\Users\HP\Desktop\intern\excel\quora_qus.xlsx',index=False)
