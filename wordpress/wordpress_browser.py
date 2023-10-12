from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

driver = webdriver.Chrome()
driver.get('https://wordpress.org/plugins/oh-add-script-header-footer/')

detail = {'name':[], 'review':[]}

sleep(3)

# links = []
# for x in range(1,26):
#     for i in range(1,22):
#         try:
#             name = driver.find_element(By.XPATH,f'//*[@id="main"]/article[{i}]/div[2]/header/h3/a').text
#             detail['name'].append(name)
#             link = driver.find_element(By.XPATH,f'//*[@id="main"]/article[{i}]/div[2]/header/h3/a').get_attribute('href')
#             detail['link'].append(link)
#             links.append(links)
#             total_review = driver.find_element(By.XPATH,f'//*[@id="main"]/article[{i}]/div[2]/div[1]/span/a').text
#             detail['review'].append(total_review)
#         except:
#             pass
#     try:
#         element = driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "next", " " ))]')
#         driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - window.innerHeight/2);",element)
#         sleep(2)

#         element.click()
#         sleep(5)
#     except:
#         pass
    
# for i in links:
#     driver.get(i)
    
dis = driver.find_element(By.XPATH,'//*[@id="tab-description"]').text
detail['name'].append(dis)
last_update = driver.find_element(By.XPATH,'//li[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//strong').text
detail['review'].append(last_update)


    
print(detail)

df = pd.DataFrame.from_dict(detail, orient='index')
df = df.transpose()

df.to_excel(r'C:\Users\HP\Desktop\intern\excel\wordpress_browser_link.xlsx',index=False)