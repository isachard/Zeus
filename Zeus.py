from Url import Url
from Parser import Parser
import pandas as pd
from bs4 import BeautifulSoup
def main():
    #Defining Variables 
    covers_url = 'https://www.covers.com/Sports/mlb/PrintSheetHtml?isPrevious=False'
    urlObj = Url(covers_url)
    parser = Parser()

    #Logic 
    bs_obj = urlObj.getBSoup()

    
    oddTable = bs_obj.findAll('tr', attrs={'class': 'trBackGround'})
    evenTable = bs_obj.findAll('tr', attrs={'class': ''})
    
    #oddThread and evenThreads are list of lists DS.
    #which contains the game threads
    oddThreads = parser.parseTable(oddTable)
    evenThreads = parser.parseTable(evenTable)

    

    
if __name__ == '__main__':
    main()

