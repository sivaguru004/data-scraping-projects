from selenium import webdriver
from time import sleep


url = "https://www.facebook.com/groups/5857109064338371/members"
driv = r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driv)
driver.get(url)

sleep(2)
email = driver.find_element('xpath','//*[@id="email"]').send_keys('email')
sleep(4)
pwd = driver.find_element('xpath','//*[@id="pass"]').send_keys('password')
sleep(5)
login = driver.find_element('xpath','//*[@id="loginbutton"]').click()
sleep(5)

driver.get('https://www.facebook.com/hariprasath17')
sleep(2)
msg = driver.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "xtvsq51", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "x1e0frkt", " " ))]').click()
sleep(5)