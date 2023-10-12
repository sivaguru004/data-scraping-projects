

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

detail = {'name':[], 'title':[], 'review':[], 'reply':[] }

a = input('enter the company name: ')

driver = webdriver.Chrome()
driver.get("https://www.trustpilot.com/")
sleep(3)

driver.find_element(By.XPATH,'//*[@id="onetrust-close-btn-container"]/button').click()
sleep(2)

search = driver.find_element(By.XPATH,'//*[@id="heroSearchContainer"]/div/div[2]/form/div/input')
search.click()
sleep(2)

search.send_keys(a)
sleep(2)

driver.find_element(By.CSS_SELECTOR,'.styles_searchButtonDesktop__1K94_').click()
sleep(3)

driver.find_element(By.CSS_SELECTOR,'.styles_resultsHeading__hG9tF+ .styles_businessUnitResult__L3bbC .styles_linkWrapper__UWs5j').click()
sleep(5)

def a():
    for i in range(4,31):
        try:
            name= driver.find_element(By.XPATH,f'//*[@id="__next"]/div/div/div/main/div/div[4]/section/div[{i}]/article/div/aside/div/a/span').text
            detail['name'].append(name)
            title = driver.find_element(By.XPATH,f'//*[@id="__next"]/div/div/div/main/div/div[4]/section/div[{i}]/article/div/section/div[2]/a/h2').text
            detail['title'].append(title)
            rvu = driver.find_element(By.XPATH,f'//*[@id="__next"]/div/div/div/main/div/div[4]/section/div[{i}]/article/div/section/div[2]/p[1]').text
            detail['review'].append(rvu)
            try:
                rpl = driver.find_element(By.XPATH,f'//*[@id="__next"]/div/div/div/main/div/div[4]/section/div[{i}]/article/div/div[2]/div[2]/p').text
                detail['reply'].append(rpl)
            except:
                detail['reply'].append('no reply')
        except:
            pass

def b():
    a()
    try:
        element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/main/div/div[4]/section/div[32]/nav/a[5]')
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - window.innerHeight/2);",element)
        sleep(2)

        element.click()
        sleep(5)
        b()
    except:
        print('done')
        pass
    
b()

df = pd.DataFrame.from_dict(detail, orient='index')
df = df.transpose()

df.to_excel(r'C:\Users\HP\Desktop\intern\excel\trustpilot.xlsx',index=False)
