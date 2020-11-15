import requests
from bs4 import BeautifulSoup

res = requests.get("https://kardecpedia.com/")
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

print(soup)



