# # import
# import requests
# from bs4 import BeautifulSoup

# url = "http://quotes.toscrape.com/"

# session = requests.Session()
# headers = {'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# 'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}

# html = session.get(url, headers=headers)
# bsObj = BeautifulSoup(html.text, 'lxml')

# # print(html.status_code)
# # print(html.headers)

# for target_cell in bsObj.select('div.quote'):
#     author_quote = target_cell.find('span', {'class':'text'}).get_text()
#     print(author_quote)
#     print("------------------")
#     author_name = target_cell.find('small', {'class':"author"}).get_text()
#     print(author_name)

# # data_from_target_cell_1 = []

# # def getQuotes():
# #     for target_cell in bsObj.select('div.quote'):
# #         # author_quote = target_cell.find('span', {'class':"text"}).get_text()
# #         author_name = target_cell.find('small', {'class':"author"}).get_text()
# #         print(author_name)



# imports
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

# handle headers and session
session = requests.Session()
headers = {'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}


# url = "http://quotes.toscrape.com"

# Create temporary data holders
Quotes_Holder = []
Author_Link_Holder = []
Author_Description_Holder = []

# First Method (Extracts data from Target cell 1)
def getQuotes(url):
    """ Scrapes data from A single 'Quote to scrape' page """
    # try catchhing any error from the server
    try:
        html = session.get(url)
    except HTTPError as e:
        return None

    # catch any errors by the page parser
    try:
        bsObj = BeautifulSoup(html.text, 'lxml')
    except AttributeError as e:
        return None

    for target_cell in bsObj.select('div.quote')[:5]:
        quote = target_cell.find('span', {'class':'text'}).get_text()
        author_of_quote = target_cell.find('small', {'class':'author'}).get_text()
        quote_tags = target_cell.find('meta', {'class':'keywords'})['content']
        link_to_author_description = target_cell.find('a')['href']

        Quotes_Holder.append({
            'Quote':quote,
            'Author':author_of_quote,
            'Tags':quote_tags
        })

        Author_Link_Holder.append(link_to_author_description)


# getQuotes("http://quotes.toscrape.com")
# print(len(Quotes_Holder))
# for i in Quotes_Holder:
#     print(i)
#     print("-----")

# for i in Author_Link_Holder:
#     print(i)
#     print("-----")




# Second Method (A method to get the next pages)


