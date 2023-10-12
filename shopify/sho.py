import  scrapy
from bs4 import BeautifulSoup
import pandas as pd
import time

df = pd.read_excel(r"D:\freelancher\shopify_link1.xlsx")
urls = list(df.Column15)


class spopify1(scrapy.Spider):
    name = 'shopify'

    start_urls = urls


    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        name = soup.find('h1', class_='tw-text-body-3xl tw-whitespace-normal tw-hyphens').text
        name = name.replace('\n','').replace('  ','')

        developer = soup.find('div',class_='tw-text-body-md').find('a', class_='tw-group tw-text-link-md tw-text-fg-primary hover:tw-text-fg-highlight-primary tw-no-underline tw-pb-2xs hover:tw-border-transparent tw-border-b-2').text
        developer = developer.replace('\n','').replace('  ','')

        review = soup.find('a', class_='tw-group tw-text-link-md tw-text-fg-primary hover:tw-text-fg-highlight-primary tw-no-underline tw-pb-2xs hover:tw-border-transparent tw-border-b-2').text
        review = review.replace('\n','').replace('  ','')

        rating = soup.find('span', class_="tw-text-body-sm tw-text-fg-secondary").text
        rating = rating.replace('\n','').replace('  ','').replace('Rating (','').replace(')','')

        about = soup.find('div',class_='tw-mt-4 tw-space-y-6').text
        about = about.replace('\n','').replace('   ','')

        discription = soup.find('div',class_='tw-flex tw-flex-col tw-gap-lg lg:tw-gap-xl').text
        discription = discription.replace('\n','').replace('   ','')

        try:
            free = soup.find_all('div', class_ = 'app-details-pricing-plan-card')[0].text
            free = free.replace('\n','').replace('   ','')
        except:
            free = 'no plan'

        try:
            silver = soup.find_all('div', class_ = 'app-details-pricing-plan-card')[1].text
            silver = silver.replace('\n','').replace('   ','')
        except:
            silver = 'no plan'

        try:
            gold = soup.find_all('div', class_ = 'app-details-pricing-plan-card')[2].text
            gold = gold.replace('\n','').replace('   ','')
        except:
            gold = 'no plane'

        try:
            platinum = soup.find_all('div', class_ = 'app-details-pricing-plan-card')[3].text
            platinum = platinum.replace('\n','').replace('   ','')
        except:
            platinum = 'no plane'
        time.sleep(2)
        yield{
            'name':name,
            'developer':developer,
            'review':review,
            'rating':rating,
            'about':about,
            'discription':discription,
            'free':free,
            'silver':silver,
            'gold':gold,
            'platinum':platinum,
        }