import requests
import bs4

def scrapWeb():

    url = "http://militera.lib.ru/1/cats/all/a/index.html"

    response = requests.get(url)

    soup = str(bs4.BeautifulSoup(response.text, "lxml"))

    # soup = soup.encode()

    with open("text","w") as file:
        file.write(soup)

if __name__=='__main__':
    scrapWeb()