# imports
import requests
import time
import dataset
from bs4 import BeautifulSoup
from urllib.request import HTTPError
from urllib.request import urljoin


class GithubScraper:
    """ Scraping Github repositories from the google page """

    # base urls for scraping
    base_url = 'https://github.com'
    start_url ='https://github.com/google'

    # declare the session and header
    session = requests.Session()
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

    # connect to the database using dataset
    db = dataset.connect('sqlite:///scrapegithub.db')

    def getTitle(self, start_url):
        """ A method that retrieves the scraping page"""

        # catch any server errors
        try:
            html = self.session.get(self.start_url, headers=self.headers)
        except HTTPError:
            print('page not Found!')

        # catch any errors thrown while parsing
        try:
            bsObj = BeautifulSoup(html.text, 'lxml')
        except AttributeError:
            print('Object not Found')
        
        title = bsObj.find("title").get_text(strip=True)
        print("")
        print('Url : {}'.format(html.url))
        print("")
        print('Status Code : {}'.format(html.status_code))
        print("")
        print('Page Title : {}'.format(title))
        print("")

    
    def scrapePage(self, url):
        """ A method that scrapes the page """
        # try catching any server errors
        try:
            html = self.session.get(url, headers=self.headers)
        except HTTPError:
            print('page not Found!')

        # catch any errors thrown while parsing the page
        try:
            bsObj = BeautifulSoup(html.text, 'lxml')
        except AttributeError:
            print('Object not Found')
        
        # get the page and loop over the target cells
        for target_cell in bsObj.select('li.public'):

            # try catching any attribute errors thrown by the parser
            try:
                repo_name = target_cell.find('h3', {'class':'wb-break-all'}).find('a').get_text(strip=True)
            except AttributeError:
                repo_name = 'None'

            # try catching any attribute errors thrown by the parser
            try:
                programming_language = target_cell.find('span', {'itemprop':'programmingLanguage'}).get_text(strip=True)
            except AttributeError:
                programming_language = 'None'

            # try catching any attribute errors thrown by the parser
            try:
                repo_description = target_cell.find('p', {'class':'break-word'}).get_text(strip=True)
            except AttributeError:
                repo_description = 'None'

            # try catching any attribute errors thrown by the parser
            try:
                members = target_cell.find('a', {'href':'/google/'+ repo_name +'/network/members'}).get_text(strip=True)
            except AttributeError:
                members = 0

            # try catching any attribute errors thrown by the parser
            try:
                stars = target_cell.find('a', {'href':'/google/'+ repo_name +'/stargazers'}).get_text(strip=True)
            except AttributeError:
                stars = 0
            
            # try catching any attribute errors thrown by the parser
            try:
                issues = target_cell.find('a', {'href':'/google/'+ repo_name +'/pulls'}).get_text(strip=True)
            except AttributeError:
                issues = 0
            
            # save the data scraped into the sqlite using the dataset library
            self.db['repositories'].insert(dict(repository=repo_name, description=repo_description, programming_lang=programming_language, members=members, stars=stars, issues=issues))

        # print the page your scraping
        print('Now scraping {}'.format(url))

        # scrape the page for the next page link
        next_page_link = bsObj.find('a', {'class':'next_page'})['href']

        # use urljoin to form a url
        next_page = urljoin(self.base_url, next_page_link)

        # try catching an error when the pages to scrape are over
        try:
            self.scrapePage(next_page)
        except UnboundLocalError:
            return None

