# imports
import requests
import csv
import time
from urllib.error import HTTPError
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Handle headers
session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

# Sites base url
base_url = "http://books.toscrape.com/"

# Temporary Data Holders
Books_Links_Holder = []
Book_Info_Holder = []

page_number = 1

# First method (gets alinks to the books)
def getBooksLinks(url):
    """ This method retrieves all the links to the books on a particular page  """
    
    global page_number

    # Try catch any errors from the server
    try:
        html = session.get(url, headers=headers)
    except HTTPError:
        return None
    
    # try catch any errors due to parsing of the html page
    try:
        bsObj = BeautifulSoup(html.text, 'lxml')
    except AttributeError:
        return None

    # loop over the target cells and get all the required details
    for target_cell in bsObj.select('article.product_pod'):
        book_title = target_cell.find('h3').find('a')['title']
        book_link = target_cell.find('h3').find('a')['href']
        book_page = urljoin(base_url, book_link)

        # send the extracted data into our temporary data holder
        Books_Links_Holder.append({
            "Title":book_title,
            "Link":book_page
        })

    # print the page currently bein scraped
    print("Now Scraping {}".format(url))

    # get the next page
    # http://books.toscrape.com/catalogue/page-2.html
    # next_page_link = bsObj.find('li', {'class':'next'}).find('a')['href']
    if page_number < 3 :
        page_number += 1
        next_page = "http://books.toscrape.com/catalogue/page-" + str(page_number) + ".html"
    
    # wait half a second before scrapin the next page
    time.sleep(.5)
    
    try:
        # scrape the next page
        getBooksLinks(next_page)
    except UnboundLocalError:
        return None


# # Test our method
# getBooksLinks(base_url)
# print('We managed to scrape {} book links including:'.format(len(Books_Links_Holder)))
# for link in Books_Links_Holder:
#     print('Link to :: {} ==> {}'.format(link['Title'], link['Link']))
#     print("-----------")

