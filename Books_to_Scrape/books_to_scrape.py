# imports
import requests
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
base_item_url = "http://books.toscrape.com/catalogue/"

# Temporary Data Holders
Books_Links_Holder = []
Book_Info_Holder = []

page_number = 1

# clean book url(ensures all our urls are standard and the same)
def cleanUrl(scrapedurl):
    split_url = scrapedurl.split('/')
    if len(split_url) <= 3:
        new_clean_url = "/".join(split_url[-2:])
        new_url = urljoin(base_item_url, new_clean_url)
    else:
        new_clean_url = "/".join(split_url[-5:])
        new_url = urljoin(base_url, new_clean_url)
    return new_url
    

# First method (gets links to the books)
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
        book_link = cleanUrl(target_cell.find('h3').find('a')['href'])
        book_page = urljoin(base_url, book_link)

        # send the extracted data into our temporary data holder
        Books_Links_Holder.append({
            "Title":book_title,
            "Link":book_page
        })

    # print the page currently bein scraped
    print("Now Scraping {}".format(url))

    # get the next page
    if page_number < 3 :
        page_number += 1
        next_page = "http://books.toscrape.com/catalogue/page-" + str(page_number) + ".html"
    
    # wait half a second before scraping the next page
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


# Second link (extracts the data from the pages)
def getBookData():
    """ Scrapes data from a single book page """
    # Loop over the list of links
    for link in Books_Links_Holder:

        # try catching any server response error
        try:
            html = session.get(link['Link'])
        except HTTPError:
            return None

        # catch any parsing errors
        try:
            bsObj = BeautifulSoup(html.text, 'lxml')
        except AttributeError:
            return None
        
        # print out the page currently eing scraped
        print("Now Scraping {}".format(link['Link']))

        # scrape thhe need info
        book_title = bsObj.find('div', {'class':'product_main'}).find('h1').get_text(strip=True)
        book_price = bsObj.find('div', {'class':'product_main'}).find('p', {'class':'price_color'}).get_text(strip=True)
        book_image_link = cleanUrl(bsObj.find('div', {'class':'item'}).find('img')['src'])
        # book_stock_availability
        book_rating = bsObj.find('div', {'class':'product_main'}).find('p', {'class':'star-rating'})['class']
        book_product_description = bsObj.find(id='product_description').find_next_sibling('p').get_text(strip=True)
        book_other_product_info = []

        # get the table info
        for table_row in bsObj.find('table', {'class':'table'}).select('tr'):
            column_title = table_row.find('th').get_text(strip=True)
            column_info = table_row.find('td').get_text(strip=True)

            # save it inside the product info data holder
            book_other_product_info.append({
                'name':column_title,
                'info':column_info
            })
        
        # send al the scraped info into the Book_Info_Holder
        Book_Info_Holder.append({
            'title':book_title,
            'price':book_price,
            'rating':book_rating[1],
            'image link':book_image_link,
            'product info':book_product_description,
            'other product info':book_other_product_info
        })


# # Test our method
# getBooksLinks(base_url)
# print('We managed to scrape {} book links :'.format(len(Books_Links_Holder)))
# getBookData()
# for i in Book_Info_Holder[:5]:
#     print(i)
#     print("------")
