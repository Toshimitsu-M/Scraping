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

elem = browser.find_element_by_xpath(
    
)

food = "かたくちいわし"
# nutrient = elem.text.replace('の働きと1日の摂取量\n', ',').replace('の働きと１日の摂取量\n', ',').replace('とは\n', ',').replace('の働きと健康効果\n', ',').replace('の定義と正しい利用法', '').replace('微量元素', 'モリブデン,マンガン,セレン,ヨウ素,クロム').replace('三大栄養素の', '').replace('ミネラル成分の', '').replace('ビタミンB6/B12', 'ビタミンB6,ビタミンB12')
browser.quit()

foods = []
foods = '\n'.join(food.split(','))
print(foods)

# tag('h2', 'contain(text='多く含む食品')')　以降のtable でスクレイピングしていいのか、表２とか　pandas   to_csv()
# caption　contain(text='表' + n)

# find_all_next(name, attrs, text, limit, **kwargs)
# first_link.find_all_next(text=True)
# # [u'Elsie', u',\n', u'Lacie', u' and\n', u'Tillie',#  u';\nand they lived at the bottom of a well.', u'\n\n', u'...', u'\n']
# find_next(name, attrs, text, **kwargs)
# first_link.find_next("p")
# # <p class="story">...</p>
#     ### **特定のテキストを含む『div』だけ取得したい**
#     `el = soup.find("div", text="プログラムが上手くなりたい")`
#     ### **ページ内の全てのh2, h3を取得したい**
#     `# 返り値はリスト
#     el = soup.find_all(['h2', 'h3'])`