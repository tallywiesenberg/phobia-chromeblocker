import requests

from bs4 import BeautifulSoup

class PageEditor:

    def __init__(self, keyword, orientation, url='https://en.wikipedia.org/wiki/Spider'):
        self.keyword = keyword
        self.url = url
        self.orientation = orientation

    def edit(self):

        #Request site data
        r = requests.get(self.url).text

        #Read site html
        soup = BeautifulSoup(r, 'html.parser')

        #Search through html to find keyword
        for i in soup.find_all('p'):
            print('------- \n')
            #Convert paragraph to string
            p = str(i)
            if self.keyword in p:
                print('Hidden Paragraph!!!')
            else:
                print(p)


