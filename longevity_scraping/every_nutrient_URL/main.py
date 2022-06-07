from selenium import webdriver
import time
import pandas as p 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
url = 'https://www.tyojyu.or.jp/net/kenkou-tyoju/eiyouso/'
browser.get(url)
time.sleep(3)

# ページのHTMLを取得
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')
url_items = soup.select('.mod-links2__list a')
for a in url_items:
    print(a['href'])
browser.quit()


