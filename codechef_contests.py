import urllib2
from tabulate import tabulate
from bs4 import BeautifulSoup

def create_table(ContestType,contests):
    print ContestType
    print tabulate(contests,headers=["Code","Name","Start","End"],tablefmt="fancy_grid")
    print "\n"


print "CODECHEF CONTESTS".center(120)

try:
  url ="https://www.codechef.com/contests"
  response = urllib2.urlopen(url)
  html = response.read()
  soup = BeautifulSoup(html,'lxml')

except Exception:
  print "Unable to connect...please try again later."
  raw_input()
  exit()

allcontests=[]
count=0

for x in soup.findAll(attrs={'class':'table-questions'}):
    contests=[]
    k=0
    for row in x.findAll('tr'):
        comp=[]
        for info in row.findAll('td'):
            if(len(info.get_text())>0):
               comp.append(info.get_text().encode("utf-8"))
        if(len(comp)>0):      
            contests.append(comp)
        k+=1    
        if(k>5):
            break
    allcontests.append(contests)    
    count+=1
    if(count == 3):
        break

create_table(">>>Present Contests",allcontests[0])
create_table(">>>Future Contests",allcontests[1])
create_table(">>>Past Contests",allcontests[2])
raw_input()
