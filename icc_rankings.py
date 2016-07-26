from bs4 import BeautifulSoup
import urllib2


titles=["ICC TEST RANKINGS","ICC ODI RANKINGS","ICC T20 RANKINGS"]
h=["Team","Matches","Points","Rating"]

my_link=urllib2.urlopen("http://www.espncricinfo.com/rankings/content/page/211271.html")
soup=BeautifulSoup(my_link,'lxml')

comptable=[]
for t in soup.find_all("table"):
  datasets=[]  
  for row in t.find_all("tr"): 
    data=[]
    for td in row.find_all("td"):
        data.append(td.get_text().encode("utf-8"))
    if len(data)==4:
        datasets.append(data)
  comptable.append(datasets)      
        

for i in range(3):
    print titles[i],'\n'
    print "%-20s%-10s%-10s%-10s"%(h[0],h[1],h[2],h[3]),'\n'
    for x in comptable[i]:
        print "%-20s%-10s%-10s%-10s"%(x[0],x[1],x[2],x[3])

    print "\n\n"    

raw_input()
