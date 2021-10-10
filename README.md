# Web Scrapping tool for Cryptocurrencies
![GitHub](https://img.shields.io/github/license/man-c/pycoingecko)

Using the Python 3 around the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [requests](https://pypi.org/project/requests/)

### Installation
## Requests 2.26.0
PyPI
```bash
python -m pip install requests
```
## Beautifulsoup4
PyPI
```bash
pip install beautifulsoup4
```

### Usage

## Requests 2.26.0

```python
import requests
r = requests.get("url")
```
## Beautifulsoup4

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup()
```

### Examples
BeautifulSoup documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc/. On this site you can view detailed information about using the BeautifulSoup library.

```shell
Enter coin: bitcoin
Bitcoin price today, BTC to USD live, marketcap and chart
CoinMarketCap: Cryptocurrency Prices, Charts And Market ...
Bitcoin (BTC) Цена, Графики, Рыночная капитализация
Bitcoin Cash price today, BCH to USD live, marketcap and chart
Global Cryptocurrency Market Charts | CoinMarketCap
All Cryptocurrencies | CoinMarketCap
Bitcoin Price (BTC) - CoinMarketCap
Bitcoin SV price today, BSV to USD live, marketcap and chart
Prijs Bitcoin (BTC) - CoinMarketCap
Bitcoin Analytics and Statistics | CoinMarketCap
```  

