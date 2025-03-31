# Web Scraper

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")

print(soup)

soup.find_all("table", class_ = "wikitable sortable jquery-tablesorter")[1]

#<table class="wikitable sortable jquery-tablesorter">
#<caption>