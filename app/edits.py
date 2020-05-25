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
        output = ''
        for i in soup.find_all('p'):
            output += '------- \n'
            #Convert paragraph to string
            p = str(i)
            if self.keyword in p:
                output += 'Hidden Paragraph!!!'
            else:
                output += p

        return output


