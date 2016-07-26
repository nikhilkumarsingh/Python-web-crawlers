from bs4 import BeautifulSoup
import urllib2
import re
from tabulate import tabulate
from math import ceil

COLUMNS=["S.no","Product","Original price(Rs.)","Discounted price(Rs.)","Discount(%)"]

def get_results(query):
      query = query.replace(' ','+')
      my_link=urllib2.urlopen("http://www.snapdeal.com/search?keyword="+query)
      soup=BeautifulSoup(my_link,'lxml')
      links=[]
      results=[]
      count=1
      pricedata=['product-desc-price','product-price']

      for product in soup.findAll(attrs={'class':'product-tuple-description'}):  
        k=[]
        k.append(count)
        links.append(product.a['href'])
        k.append(product.p['title'][:50])
        for i in range(2):
          flag=0     
          for prices in product.findAll(attrs={'class':pricedata[i]}):
            price=prices.get_text().encode("utf-8")
            price = re.sub('[^0-9]+','', price)
            k.append(int(price))
            flag=1
            break
          if (flag == 0):
            k.append(0)
        if(k[2] == 0):
            k[2]=k[3]
        k.append(ceil((float(k[2]-k[3])/k[2])*100))      
        results.append(k)
        count+=1
        if(count>10):
            break
      return results


if __name__ == "__main__":
      query = raw_input("What do you want to search for? ")
      results=get_results(query)
      print tabulate(results,headers=COLUMNS,tablefmt="fancy_grid")
      #print links
