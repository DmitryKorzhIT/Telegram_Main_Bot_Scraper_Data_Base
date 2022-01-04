import requests
from bs4 import BeautifulSoup as BS

f = open("data.csv", 'a')
page = 1

while True:
    r = requests.get('https://stopgame.ru/review/new/izumitelno/p' + str(page))
    html = BS(r.content, 'html.parser')
    items = html.select(".items > .article-summary")

    if(len(items)):
        for el in items:
            # print(el, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            title = el.select('.caption > a')
            f.write(title[0].text + "\n")
        page += 1
    else:
        break