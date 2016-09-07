'''
A web crawler using selenium web-driver to extract dynamic html content from codechef. 
'''
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox()


contest_name = 'SEPT16'
page=1

driver.get('https://www.codechef.com/rankings/'+contest_name+'?filterBy=Institution%3DDelhi%20Technological%20University&order=asc&sortBy=rank&page='+str(page))

html = driver.page_source
soup = BeautifulSoup(html)

table = soup.find("table",attrs = {'class':'dataTable'})
tbody = table.find("tbody")

users=[]

for row in tbody.findAll('tr'):
    student={}
    student['name']=row.find('div',attrs={'class':"user-name"}).get_text()
    student['data']=[]
    for col in row.findAll('td',attrs={'class':"num"}):
        student['data'].append(col.get_text())
    users.append(student)

print "done"
