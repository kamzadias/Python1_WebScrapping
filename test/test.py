from Assigment2 import Scrapper

scrapper = Scrapper()
list = scrapper.get(input("Enter coin: "))

for item in list:
   print(item.text.strip())
