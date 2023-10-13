import requests,openpyxl
from bs4 import BeautifulSoup

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title='Top 250 MOVIES'
sheet.append(['RANK','MOVIES','YEAR','RATING'])

try:
    source = requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status() #it throws the error if the link is not

    soup=BeautifulSoup(source.text,'html.parser')
    movies=soup.find('tbody',class_='lister-list').find_all('tr')
    for namemovie in movies:
        name=namemovie.find('td',class_='titleColumn').a.text
        rank=namemovie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
        year=namemovie.find('td',class_='titleColumn').span.text.strip('()')
        rating =namemovie.find('td',class_='ratingColumn imdbRating').strong.text
except Exception as e:
    print(e)

excel.save('Top 250 IMDB.xlsx')