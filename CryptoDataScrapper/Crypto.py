import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import os
from time import sleep

url ='https://www.coingecko.com'
logo = '---------- Crypto Data Scrapper ----------'; 
headers = {
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
   'accept-language': 'en-US,en;q=0.7',
   'Connection':'keep-alive',
   'upgrade-insecure-requests': '1',
   'cache-control': 'max-age=0'
}

tables=[]
os.system('cls')
print(logo)
Pages = int(input("-> How many Pages you want to Extract 1-133: "))
if Pages > 0 or Pages < 133:
        
    for i in range(1,Pages):
        print("Scraping Page: {}".format(i))
        params={
            'page': Pages
        }
        response = requests.get(url,headers=headers,params=params)
        soup= BeautifulSoup(response.content, 'html.parser')
        tables.append(pd.read_html(str(soup))[0])

    finalTable = pd.concat(tables)
    finalTable = finalTable.loc[:,finalTable.columns[1:-1]]
    finalTable.to_csv("Data.csv",index=False)
else:
    print("Pages out of Range.")
    sleep(1)
    os.system('python3 Crypto.py')
