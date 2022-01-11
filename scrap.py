import requests
import bs4

url = "http://militera.lib.ru/1/cats/all/sch/index.html"

response = requests.get(url)

soup = str(bs4.BeautifulSoup(response.text, "lxml"))

# soup = soup.encode()

with open("text","w") as file:
    file.write(soup)