import scrapy
from bs4 import BeautifulSoup

class JustDialSpider(scrapy.Spider):
    name = 'justdial_spider'
    start_urls = ['https://www.justdial.com/Coimbatore/Solar-Panel-Dealers/nct-10444071']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    }
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        so = soup.find_all('div',class_ ='resultbox_textbox')
        for i in so:

            try:
                name = i.find('a',class_="resultbox_title_anchor line_clamp_1 font22 fw500 color111").text.strip()
                link = i.find('a',class_="resultbox_title_anchor line_clamp_1 font22 fw500 color111").get('href')
                v = i.find('div', class_='jdicon results_jdverified animated fadeIn')
                if v is not None:
                    verified = 'yes'
                else:
                    verified = 'no'

                t = i.find('div', class_='jdicon results_jdtrusted mr-5 animated fadeIn')
                if t is not None:
                    trust = 'yes'
                else:
                    trust = 'no'
            except:
                pass
            yield {
                'name': name,
                # 'link': 'https://www.justdial.com'+link
                'trust': trust,
                'verified': verified
                }

