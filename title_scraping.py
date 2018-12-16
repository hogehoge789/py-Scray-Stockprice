import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.scrapmagazine.com/')
soup = BeautifulSoup(response.text, 'lxml')
title = soup.title.string
print(title)
