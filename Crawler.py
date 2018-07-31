import requests
import re
from bs4 import BeautifulSoup
base_url = "https://www.ptt.cc/"
home_url = "https://www.ptt.cc/bbs/Lifeismoney/index.html"
res = requests.get(home_url)
soup = BeautifulSoup(res.text, 'html.parser')

for news in soup.find_all(class_='r-ent'):
    date = news.find('div', attrs={'class': 'date'}).text
    author = news.find('div', attrs={'class': 'author'}).text
    if news.find('a'):
        title = news.find('div', attrs={'class': 'title'}).text
        path = news.find('a')['href']


    print(title, date, path, author)
