from bs4 import BeautifulSoup
import requests

SEARCH_URL = 'https://www.googleapis.com/customsearch/v1?key=XXXXXXXXXXX&cx=XXXXXXXXXXXXXXXXXXXXX&q='

def get_lyrics(url):
    if 'http' not in url:
        url='http://' + url
    r=requests.get(url)
    soup=BeautifulSoup(r.content)
    soup=str(soup).replace("<br/> ", "\n")
    soup=BeautifulSoup(soup)
    details=[]
    for detail in soup.findAll('p'):
        details.append(detail.get_text())

    '''
    metadata={}
    for data in details[3].split('\n'):
        info=data.split(':')
        metadata[info[0]]=info[1].strip()
    data.append(metadata)
    '''
    lyrics = '\n\n'.join(para for para in details)
    
    
    return lyrics

def search_song(query):
    r = requests.get(SEARCH_URL + query.replace(' ','+'))
    items=r.json()['items']
    result=[]
    for item in items[:3]:
        data={}
        data['title'] = item['title']
        data['url'] = item['formattedUrl']
        result.append(data)
    return result    


while 1:
    url = search_song(raw_input())[0]['url']
    print get_lyrics(url)
