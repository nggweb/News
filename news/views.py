from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Getting news from Times of India
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_news = []

for news in toi_soup.find_all('div', class_='brief_box'):
    # Extracting news image
    try:
        image = news.find('img')['src']
    except:
        image = 'None'
    # Extracting news heading
    try:
        heading = news.find('h2').text
    except:
        heading = 'None'
    # Extracting news paragraph
    # 
    try:
        para = news.find('div', class_='brief').text.strip()
    except:
        para = 'None'

    toi_news.append({'image': image, 'heading': heading, 'para': para})


#Getting news from Hindustan times

ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news})