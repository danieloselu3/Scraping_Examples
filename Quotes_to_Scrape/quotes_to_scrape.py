# imports
import requests
import csv
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
    except HTTPError:
        return None

    # catch any errors by the page parser
    try:
        bsObj = BeautifulSoup(html.text, 'lxml')
    except AttributeError:
        return None

    for target_cell in bsObj.select('div.quote'):
        quote = target_cell.find('span', {'class':'text'}).get_text(strip=True)
        author_of_quote = target_cell.find('small', {'class':'author'}).get_text(strip=True)
        quote_tags = target_cell.find('meta', {'class':'keywords'})['content']
        link_to_author_description = target_cell.find('a')['href']

        Quotes_Holder.append({
            'Quote':quote,
            'Author':author_of_quote,
            'Tags':quote_tags
        })

        Author_Link_Holder.add(link_to_author_description)
    
    # catch any attribute error thrown by bs4 incase our target is empty
    try:
        next_url = bsObj.find('li', {'class':'next'}).find('a')['href']
    except AttributeError:
        return None

    # next page functionality
    if next_url is not None:
        next_page_to_scrape = base_url + next_url
        getQuotes(next_page_to_scrape)
    else:
        print('no more pages to scrape')

# TEST OUR getQuotes METHOD

# getQuotes("http://quotes.toscrape.com")
# print(len(Quotes_Holder))
# for i in Quotes_Holder[-1:]:
#     print(i)
#     print("-----")
# print(len(Author_Link_Holder))
# for i in Author_Link_Holder[:5]:
#     print(i)
#     print("-----")


# Second Method (getAuthorInfo)
def getAuthorInfo():
    """ Scapes the Authors information """
    # Loop over the global Author_Link_Holder list, 
    # that will be populated by the getQuotes Method
    for author_link in Author_Link_Holder:
        # concatenate a link to the author's page
        author_target_page = base_url + author_link

        # get the authors page and create a beautiful soup object
        # catch any error from the server
        try:
            html = session.get(author_target_page)
        except HTTPError:
            return None

        # catch any attribute error
        try:
            bsObj = BeautifulSoup(html.text, 'lxml')
        except AttributeError:
            return None

        # extract the required data
        author_name = bsObj.find('h3', {'class':'author-title'}).get_text(strip=True)
        author_date_of_birth = bsObj.find('span', {'class':'author-born-date'}).get_text(strip=True)
        author_place_of_birth = bsObj.find('span', {'class':'author-born-location'}).get_text(strip=True)
        author_description = bsObj.find('div', {'class':'author-description'}).get_text(strip=True)

        # append the data into the global Author_Description_Holder
        Author_Description_Holder.append({
            'Author':author_name,
            'Date of Birth':author_date_of_birth,
            'Place of Birth':author_place_of_birth,
            'Author Description':author_description
        })

# TEST OUR getAuthorInfo METHOD

# getQuotes("http://quotes.toscrape.com")
# getAuthorInfo()
# for i in Author_Description_Holder[:3]:
#     print(i)
#     print('------')


def saveData():
    # Save Quotes Scraped

    # save in a variable the names of your columns
    columns = ['Quote', 'Author', 'Tags']
    try:
        with open('Quotes_to_Scrape.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
            for quote in Quotes_Holder:
                writer.writerow(quote)
    except IOError:
        return None
    print('Quote data saved!')

    # Save Author info scraped
    author_columns = ['Author', 'Date of Birth', 'Place of Birth', 'Author Description']
    try:
        with open('Author_info.csv', 'w') as authorfile:
            writer = csv.DictWriter(authorfile, fieldnames=author_columns)
            writer.writeheader()
            for info in Author_Description_Holder:
                writer.writerow(info)
    except IOError:
        return None
    print('Author information saved!')



# Obtain the data from the website

getQuotes("http://quotes.toscrape.com")
getAuthorInfo()
saveData()