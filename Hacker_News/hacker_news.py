# imports
import requests
from bs4 import BeautifulSoup

# handling the scraper header
session = requests.Session()
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}

url = "https://news.ycombinator.com/"

html = session.get(url, headers=headers)
bsObj = BeautifulSoup(html.text, 'lxml')

print(html.status_code)
# print(html.headers)
print(bsObj.find('title').get_text())