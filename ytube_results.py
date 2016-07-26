import urllib2
import os
from bs4 import BeautifulSoup



def get_videos(query,nresults):
    vid_data=[]
    url = "https://www.youtube.com/results?search_query=" + query.replace(' ','+')
    for _ in range(1000):
       response = urllib2.urlopen(url)
       html = response.read()
       soup = BeautifulSoup(html,'lxml')
    
       for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
         data={}  
         data['url']='https://www.youtube.com' + vid['href']
         data['info']=vid.get_text().encode("utf-8")
         vid_data.append(data)
         if(len(vid_data)>nresults):
             break
       if(len(vid_data)>nresults):
             break
    return vid_data


if __name__ == "__main__":
    query =raw_input("Enter search text:")
    videos=get_videos(query,10)
    for video in videos:
        print video['info'],video['link']
