
import csv
import urllib.request
import io
import json
from pprint import pprint


stock_list = ['AAPL','AAOI','AET','AMD','AMZN','AVGO',
'BABA','C','CFG','CSCO','CTXS',
'DIS','FB','GOOG','INTC','LSCG',
'LMT','MSFT','MU',
'NBN','NFLX','NVDA','OLED','ORCL','PEP',
'QCOM','SBUX','TSLA','TWTR','UNH']
company_list = ''
for company in stock_list: company_list = company_list + company + "+"
url = "http://download.finance.yahoo.com/d/quotes.csv?s="+company_list+"&f=na"
response = urllib.request.urlopen(url)
cr = csv.reader(io.TextIOWrapper(response))
numbers = []
symbol = []
for row in cr:
  try:
    numbers.append(float(row[1]))
    symbol.append(row[0])
  except ValueError:
    row = -1

#Print stocks with name and price
#for sym, num in zip(symbol, numbers):
#  print (sym, ': ', num)

dictionary = dict(zip(list, numbers))
#print (dictionary)

  #write stock prices to file for compairson
with open('stockPrices.json', 'w') as f:
   json.dump(dictionary, f)

# Reading data back
with open('stockPrices.json', 'r') as f:
  data = json.load(f)
  pprint(data)

