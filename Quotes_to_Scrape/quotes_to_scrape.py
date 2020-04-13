# imports
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

# handle headers and session
session = requests.Session()
headers = {'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}

# base url
base_url = "http://quotes.toscrape.com"

# Create temporary data holders
Quotes_Holder = []
Author_Link_Holder = set()
Author_Description_Holder = []

# First Method (Extracts data from Target cell 1)
def getQuotes(url):
    """ Scrapes data from A single 'Quote to scrape' page """
    # try catching any error from the server
    try:
        html = session.get(url)
    except HTTPError as e:
        return None

    # catch any errors by the page parser
    try:
        bsObj = BeautifulSoup(html.text, 'lxml')
    except AttributeError as e:
        return None

    for target_cell in bsObj.select('div.quote'):
        quote = target_cell.find('span', {'class':'text'}).get_text()
        author_of_quote = target_cell.find('small', {'class':'author'}).get_text()
        quote_tags = target_cell.find('meta', {'class':'keywords'})['content']
        link_to_author_description = target_cell.find('a')['href']

        Quotes_Holder.append({
            'Quote':quote,
            'Author':author_of_quote,
            'Tags':quote_tags
        })

        Author_Link_Holder.add(link_to_author_description)
    
    # catcch any attribute error thrown by bs4 incase our target is empty
    try:
        next_url = bsObj.find('li', {'class':'next'}).find('a')['href']
    except AttributeError as e:
        return None

    # next page functionality
    if next_url is not None:
        next_page_to_scrape = base_url + next_url
        getQuotes(next_page_to_scrape)
    else:
        print('no more pages to scrape')


# getQuotes("http://quotes.toscrape.com")
# print(len(Quotes_Holder))
# for i in Quotes_Holder[-1:]:
#     print(i)
#     print("-----")
# print(len(Author_Link_Holder))
# for i in Author_Link_Holder:
#     print(i)
#     print("-----")



