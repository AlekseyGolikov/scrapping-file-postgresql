import requests
import bs4

url = "http://militera.lib.ru/1/cats/all/sch/index.html"

def scrapWeb():
    
    response = requests.get(url)

    soup = str(bs4.BeautifulSoup(response.text, "lxml"))

    # soup = soup.encode()

    with open("text","w") as file:
        file.write(soup)

if __name__=='__main__':
    scrapWeb()