import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
map = input("what do you want to search: ")
search = map.replace(" ","+")
url = f'https://www.google.com/maps/search/{search}'

driv = r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(driv)
browser.get(url)

soup = BeautifulSoup(browser.page_source,'html.parser')
store = soup.find_all('div',class_="Nv2PK THOPZb CpccDe")

empty = []
save = []
details={"Name":[],"Link":[],"Address":[],"Rate":[],"Review":[],"Contact":[]}

for i in store:
    link=i.find("a",class_="hfpxzc").get("href")
    name = i.find('div',class_="qBF1Pd fontHeadlineSmall").text

    try:
        rate = i.find('span',class_="MW4etd").text
        review = i.find('span',class_="UY7F9").text.replace('(','').replace(')','')
        details["Rate"].append(rate)
        details["Review"].append(review)
    except:
        details["Rate"].append("NAN")
        details["Review"].append("NAN")
    r=requests.get(link)
    Soup=BeautifulSoup(r.content,"html.parser")
    address=Soup.find("meta",attrs={"itemprop":"name"}).get("content")
    
    details["Name"].append(name)
    details["Link"].append(link)
    details["Address"].append(address)

    a = i.find_all('div',class_="W4Efsd")
    for x in a[3]:
        b = x.find_all('span')
        for y in b:
            ab = y.text
            empty.append(ab)
    phone = empty[-1]
    Phone = phone.replace(" ",'')
    save.append(Phone)
    empty.clear()    

for nu in save:
    try:
        nu = int(nu)
        details['Contact'].append(nu)
    except:
        details['Contact'].append('No Contact')

df = pd.DataFrame(details)
print(df)

#df.to_excel(r'C:\Users\HP\Desktop\intern\excel\google_my_business5.xlsx',index=False)

browser.close()