from urllib import request as rq
from bs4 import BeautifulSoup

class Url(object):

    def __init__(self, url ):
        self.url = url

    def getUrl(self):
        return self.url

    def getBSoup(self):
        try:
            data = BeautifulSoup(rq.urlopen('https://www.covers.com/Sports/mlb/PrintSheetHtml?isPrevious=False'),'lxml')
            return data #data is a bs4 obj
        except rq.HTTPError:
            print('Error Requesting Webpage ' + rq.HTTPError)
        return None
