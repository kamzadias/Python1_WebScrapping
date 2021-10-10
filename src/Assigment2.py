import requests
from bs4 import BeautifulSoup

class Scrapper:
   def get(self, coin):
      r = requests.get("https://www.google.com/search?q=site%3Acoinmarketcap.com+"+coin).text
      
		  #r2=requests.get("https://coinmarketcap.com/currencies/'+coin+'/news/").text
      #If needed to get the paragpaphs from the coinmarketcap website itself, then use this link

      soup = BeautifulSoup(r, 'html.parser')
      text = soup.find_all("h3")

      #text = soup.find_all("div")
      #If needed to get the paragpaphs from the coinmarketcap

      return text

scrapper = Scrapper()
list = scrapper.get(input("Enter coin: "))

for item in list:
   print(item.text.strip())
