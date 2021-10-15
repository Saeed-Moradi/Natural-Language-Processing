import scrapy_user_agents
from bs4 import BeautifulSoup
import requests
import urllib.request, sys, time
import pandas as pd
import scrapy
import csv
URL = 'http://www.blogfa.com/'
try:  # Exception handling
    page = requests.get(URL)
except Exception as e:
    print(sys.exc_info())
soup = BeautifulSoup(page.content, 'html.parser')
all_blogs = soup.find_all('a', target='_blank')
links = []
for link in all_blogs:
    links.append(link.get('href'))
print(links)
# f = open('BlogfaDataset.csv', 'w', newline='')
# columns = ['Blog Address', 'Blog Content 2', 'Blog Content 3', 'Blog Content 4', 'Blog Content 5', 'Blog Content 6',
#            'Blog Content 7', 'Blog Content 8', 'Blog Content 9', 'Blog Content 10']
# writer = csv.writer(f)
# writer.writerow(columns)
for link in links:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_titles = soup.find_all('a')
    titles = []
    for title in all_titles:
        if len(titles) != 10 and title.getText() != '+':
            titles.append(title.getText())
    print(titles)
    # writer = csv.writer(f)
    # writer.writerow(titles)
    titles.clear()
