import re
import urllib
import urllib2
import os
import shutil
from bs4 import BeautifulSoup
from subprocess import call
import ctypes


###################################################################################################
def download_song(url):
  print "\n\n\nDownload for your song is starting...\n"
  try:
    command ="youtube-dl --extract-audio --audio-format mp3 "+url
    call(command, shell=False)
    result=ctypes.windll.user32.MessageBoxA(0, "Download for your song is complete!", "Alert", 0)
  except Exception:
    result=ctypes.windll.user32.MessageBoxA(0, "Download failed!", "Alert", 0)

    
def find_song(textToSearch):
  for _ in range(1000):
    query = urllib.quote(textToSearch+" video song")
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,'lxml')
    vid_url=[]
    vid_info=[]

    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
      vid_url.append('https://www.youtube.com' + vid['href'])
      vid_info.append(vid.get_text().encode("utf-8"))

    if(len(vid_url)>10):
      break

  for i in range(len(vid_url)):
    result=ctypes.windll.user32.MessageBoxA(0, "Start download for song:\n"+vid_info[i],str(len(vid_url))+" results found!", 3)
    if(result == 6):
      download_song(vid_url[i])
      break
    elif(result == 7):
      continue
    else:
      break
##################################################################################################

def page_one():
  os.system('cls')
  print "Show top hindi songs for:"
  types=["today","yesterday","thisweek","thismonth","alltime"]
  for i in range(5):
     print str(i+1)+'.',types[i]
  k=int(raw_input("\nEnter type:"))-1
  return types[k]

def page_two(category):
  site_address="http://www.songsmp3.com/category/top?type="+category
  my_link=urllib2.urlopen(site_address)
  soup=BeautifulSoup(my_link,'lxml')
  names=[]
  artists=[]
  for song in soup.find_all("div","link-item"):
    for info in song.find("div","link"):
        names.append(info.get_text().encode("utf-8"))
    for artist in song.find_all("div","item-artist"):
        artists.append(artist.get_text().encode("utf-8"))

  for i in range(21):
    artists[i] = re.sub('[^A-Za-z0-9,]+',' ', artists[i] ) #cleaning artists list...

  for _ in range(10):
    os.system('cls')
    print "Showing top hindi songs for:"+category,'\n'
    for i in range(21):
      print "%-3s%-60s%-10s%-10s"%("x"+str(i+1),names[i][2:],":::::",artists[i][:50])
    n=int(raw_input("\nEnter the song code to download or 0 to go back:"))
    if(n):
     find_song(names[n-1])
    else:
      break


for _ in range(10000):    
  page_two(page_one())





