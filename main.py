

import csv
import urllib.request
import io
import json
from pprint import pprint
from StockTracker import StockTracker

def main():
  '''main class to handle stock data'''
  print ("Hello Stock World")
  stocks = StockTracker()
  stocks.add_ticker('AMD', True)
  #stocks.add_ticker('AAPL')
  #stocks.add_ticker('BABA', True)
  stocks.add_ticker('C', True)
  stocks.add_ticker('NVDA', True)
#  stocks.add_ticker('OLED')
  stocks.add_ticker('RIO', True)
#  stocks.add_ticker('GDXJ')
  stocks.add_ticker('IAG', True)
#  stocks.add_ticker('NFLX')
#  stocks.add_ticker('TSLA')
#  stocks.add_ticker('DIS')
#  stocks.add_ticker('FB')
#  stocks.add_ticker('AVGO')
#  stocks.add_ticker('GOOGL')
#  stocks.add_ticker('AAOI')
#  stocks.add_ticker('JNJ')
#  stocks.add_ticker('NBN')
#  stocks.add_ticker('CFG')
#  stocks.add_ticker('SBUX')

#scrape stock data
  stocks.construct_url ('nad1t1c1ohgv', stocks.company_list)
  
  # build stock data
  stocks.build_stock_data()
  
  # Write stock data to JSON file
  stocks.write_JSON()
  
  print ("Goodbye Stock World")

if __name__ == '__main__':
  main()