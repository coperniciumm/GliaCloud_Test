import requests
import re
from bs4 import BeautifulSoup

base_url = "https://www.ptt.cc"
home_url = base_url + "/bbs/Lifeismoney/index.html"
res = requests.get(home_url)
soup = BeautifulSoup(res.text, 'html.parser')

for news in soup.find_all(class_='r-ent'):
    story_title = news.find('div', attrs={'class': 'title'}).text
    #story_path = news.find_all('div', attrs={'class': 'title'}).find('a')['href']
    #story_path = news.find('div', attrs={'class': 'title'}).find(href=re.compile("^/bbs\d+"))
    story_date = news.find('div', attrs={'class': 'date'}).text

    print(story_title, story_date)
    #print(news.text)
