import requests
from bs4 import BeautifulSoup

def ScrapeData(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html5lib')   #lxml gives only 94 results :(

    table = soup.find('tbody')
    
    chart = []
    for row in table.findAll('tr'):
        movie={}
        for col in row.findAll('td'):
            if col['class'] == ['titleColumn']:
                data = col.get_text().split('\n')
                movie['rank'] = data[1].strip()[:-1]
                movie['name'] = data[2].strip()
                movie['year'] = data[3].strip()[1:-1]
            if col['class'] == ['ratingColumn','imdbRating']:
                movie['rating'] = col.get_text().replace('\n','')
        chart.append(movie)        
    print len(chart)
    return chart


def CrawlIMDB():
    BASE_URL = 'http://www.imdb.com/chart/'
    CATEGORIES = ['top-indian-movies','top','toptv','bottom']
    chartDB = []
    for category in CATEGORIES:
        chart = {}
        chart['category'] = category
        url = BASE_URL + category
        chart['table'] = ScrapeData(url)
        chartDB.append(chart)
    return chartDB


myDB = CrawlIMDB()
        

