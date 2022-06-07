from selenium import webdriver
import time
import pandas as p 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
url = 'https://www.tyojyu.or.jp/net/kenkou-tyoju/eiyouso/'
browser.get(url)
time.sleep(3)

elem = browser.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/ul')

# replaceを配列で見やすくしたい。
# 配列変数をメソッドにしたい。
#そのためにnutrientのコードをtypeとかテキストで読み込みたい。
nutrient_replace = []


nutrient = elem.text.replace('の働きと1日の摂取量\n', ',').replace('の働きと１日の摂取量\n', ',').replace('とは\n', ',').replace('の働きと健康効果\n', ',').replace('の定義と正しい利用法', '').replace('微量元素', 'モリブデン,マンガン,セレン,ヨウ素,クロム').replace('三大栄養素の', '').replace('ミネラル成分の', '').replace('ビタミンB6/B12', 'ビタミンB6,ビタミンB12')
browser.quit()

nutrients = []
nutrients = '\n'.join(nutrient.split(','))
print(nutrients)
