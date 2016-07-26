from bs4 import BeautifulSoup
import urllib2
import os
from random import randint
import re


def generate_quotes(npages):
    quotes=[]
    for i in range(npages):
      site_address='http://www.values.com/inspirational-quotes?page='+str(i)
      response=urllib2.urlopen(site_address)
      html=response.read()
      soup=BeautifulSoup(html,'lxml')

      for q in soup.findAll('div'):
         for info in q.findAll('h6'):
            quotes.append(info.get_text().encode("utf-8"))
        
    print len(quotes)
    qfile=open('quotes.txt','w')
    for x in quotes:
      qfile.write(x+'\n\n\n');
    qfile.close()

def generate_random_quote():
    qfile=open('quotes.txt','r')
    myquotes=list(qfile.read().split('\n\n\n'))
    qfile.close()
    QuoteOfTheDay=myquotes[randint(0,len(myquotes)-1)]
    print QuoteOfTheDay
    raw_input()

if __name__ == "__main__":
    #generate_quotes(3)
    generate_random_quote()

