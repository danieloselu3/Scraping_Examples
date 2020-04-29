import requests
import time
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

    
    def scrapePage(self):
        repo_holder = []

        try:
            html = self.session.get(self.start_url, headers=self.headers)
        except HTTPError:
            print('page not Found!')

        try:
            bsObj = BeautifulSoup(html.text, 'lxml')
        except AttributeError:
            print('Object not Found')
        
        for target_cell in bsObj.select('li.public'):
            repo_name = target_cell.find('h3', {'class':'wb-break-all'}).find('a').get_text(strip=True)
            try:
                repo_description = target_cell.find('p', {'class':'break-word'}).get_text(strip=True)
            except AttributeError:
                repo_description = 'None'

            programming_language = target_cell.find('span', {'itemprop':'programmingLanguage'}).get_text(strip=True)
            members = target_cell.find('a', {'href':'/google/'+ repo_name +'/network/members'}).get_text(strip=True)

            try:
                stars = target_cell.find('a', {'href':'/google/'+ repo_name +'/stargazers'}).get_text(strip=True)
            except AttributeError:
                stars = 0
            
            try:
                issues = target_cell.find('a', {'href':'/google/'+ repo_name +'/pulls'}).get_text(strip=True)
            except AttributeError:
                issues = 0

            repo_holder.append({
                'repository' : repo_name,
                'description' : repo_description,
                'programming Lang' : programming_language,
                'members' : members,
                'stars' : stars,
                'issues' : issues
            })

        for i in repo_holder:
            print(i)
            print("")
            
            




