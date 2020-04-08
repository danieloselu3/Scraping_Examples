# imports
import requests
from bs4 import BeautifulSoup

# handling the scraper header
# explicitly sending up the header enables us to look like a real browser
# when sending the request to the server.
session = requests.Session()
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}

# Site we are scraping
url = "https://news.ycombinator.com/"

# Send a GET request to the site(url), store it in a html object, 
# then create a BeautifulSoup object bsObj
html = session.get(url, headers=headers)
bsObj = BeautifulSoup(html.text, 'lxml')

# an empty list to hold our scraped data
articles = []

# looping inside the target cell to pick up individual data
for target_cell in bsObj.find('table', {"class":"itemlist"}).find_all('tr', {'class':'athing'}, limit=5):
    article_title = target_cell.find('a', {'class':'storylink'}).get_text()
    article_link = target_cell.find('a', {'class':'storylink'})['href']
    article_id = target_cell['id']
    article_rank = target_cell.find('span', {'class':'rank'}).get_text()
    primary_site = target_cell.find('span', {'class':'sitestr'}).get_text()

    # send or scraped data into the articles list holder
    articles.append({
        'rank':article_rank,
        'id':article_id,
        'title':article_title,
        'link':article_link,
        'primary_site':primary_site
    })

# print out our data
for article in articles:
    print(article)
    print("")