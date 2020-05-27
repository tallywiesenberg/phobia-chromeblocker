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
        output = {}
        for idx, item in enumerate(soup.find_all('p')):
            #Convert paragraph to string
            p = str(item)
            if self.keyword in p:
                output[idx] = 'Hidden Paragraph!'
            else:
                output[idx] = p

        return output


