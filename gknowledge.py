import requests
import json
import urllib

key="AIzaSyApuFoKxVMRQ2einlsA0rkx2S4WJjJIh34"

def get_wikidata(query):
    query=raw_input()
    r=requests.get('https://www.wikidata.org/w/api.php?action=wbsearchentities&search='+query+'&language=en&format=json')
   #r=requests.get('https://www.wikidata.org/w/api.php?action=wbgetentities&id='+id+'&languages=en&format=json')
    print r.json()


def get_kgsearch_result(query):
    url='https://kgsearch.googleapis.com/v1/entities:search?query='+query+'&key='+key+'&limit=1&indent=True'
    r=requests.get(url)
    mydata={}

    try:
      data=r.json()['itemListElement'][0]['result']
    except:
      return mydata

    try:
      mydata['type']=data['@type'][0]
    except:
      mydata['type']=None;  
    try:
      mydata['name']=data['name']
    except:
      mydata['name']=None  
    try:
      mydata['image']=data['image']['contentUrl']
    except:
      mydata['image']=None
    try:  
      mydata['description']=data['description']
    except:
      mydata['description']=None  
    try:
      mydata['shortdesc']=data['detailedDescription']['articleBody']
    except:
      mydata['shortdesc']=None  

    return mydata

