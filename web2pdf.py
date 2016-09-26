import requests
from bs4 import BeautifulSoup


BASE_URL = "http://www.web2pdfconvert.com/engine?cURL="


def web2pdf(PAGE_URL,file_name):
    URL = BASE_URL + PAGE_URL
    response = requests.get(URL)
    soup = BeautifulSoup(response.content)
    PDF_URL = soup.find('a')['href']
    PDF_RESP = requests.get(PDF_URL)

    with open(file_name+'.pdf','wb') as f:
        f.write(PDF_RESP.content)

    return



def main():
    PAGE_URL = raw_input("Enter the URL of the webpage you want to convert to a pdf:")
    file_name = raw_input("Enter the file name:")
    web2pdf(PAGE_URL,file_name)
    print "Done"

if __name__ == "__main__":
    main()
