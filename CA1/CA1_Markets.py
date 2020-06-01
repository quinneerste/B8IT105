# -*- coding: utf-8 -*-
"""
Created on Mon Apr 3 18:42:20 2020

@author: quinn
"""

import requests
from bs4 import BeautifulSoup


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Referer': 'https://www.google.com/',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

#response = requests.get('https://www.marketwatch.com/story/these-stocks-have-been-crushed-since-the-coronavirus-began-to-take-down-the-us-market-2020-02-27', headers=headers)

def market_scrape():
    response = requests.get('https://www.marketwatch.com/story/these-stocks-have-been-crushed-since-the-coronavirus-began-to-take-down-the-us-market-2020-02-27', headers=headers)
    B_S = BeautifulSoup(response.content, 'html.parser')
    return B_S

def table_info(B_S):
	rows = B_S.find_all('tr')
	for row in rows: 
		row = row.text.strip().replace('\n',',').replace(',,', ',')
		if len(row) == 0:
			print('"0"',)
		else:
			print(row,)

def main():
    B_S = market_scrape()
    table_info(B_S)
    
if __name__ == '__main__':
    main()
