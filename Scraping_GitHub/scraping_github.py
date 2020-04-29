import requests
from bs4 import BeautifulSoup
from urllib.request import HTTPError


class GithubScraper:
    start_url = 'https://github.com/google'

    session = requests.Session()
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


    def getTitle(self):
        try:
            html = self.session.get(self.start_url, headers=self.headers)
        except HTTPError:
            print('page not Found!')

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

    
    # def scrapePage(self):



