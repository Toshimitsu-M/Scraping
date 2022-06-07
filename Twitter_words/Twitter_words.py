import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# URLの指定
html = urlopen("https://primenumbers.co.jp/blog/twitterads/twitter_interesting/")
bsObj = BeautifulSoup(html, "html.parser")

# テーブルを指定
# figure class="wp-block-table">
table = bsObj.findAll("figure", {"class":"wp-block-table"})[0]
rows = table.findAll("tr")

with open("twitter_words.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
