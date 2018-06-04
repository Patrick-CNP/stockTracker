#!/usr/bin/python3

import re
import sys
import time
import requests
import csv
import urllib.request
import io
import json
from pprint import pprint
import pdb


class StockTracker:
  

  def __init__(self):
    self.watch_list = []  # list of stock symbols to pass to URl
    self.investment_list = [] # list of My current investments
    self.stocks = {} # dictionary of stock data sorted by symbol
    self.stock_name = [] # list of stock names
    self.stock_price = [] # list of stock prices
    self.percent_change = [] # list of percent changed
    self.open = [] # list of open prices
    self.high = [] # list of highs for the stock
    self.low = [] # list of lows for the stock
    self.stock_data = {} # dictionary of stock names and their prices
    self.my_list = {} # dictionary of stock symbols I own sorted by symbol
    self.company_list = ''


#adds a new stock ticker symbol to the list
  def add_ticker(self, symbol, my_list=False):
  
    if my_list == True:
      self.investment_list.append(symbol)
      self.watch_list.append(symbol)
      self.investment_list.sort()
      self.investment_list.sort()
    else:
      self.watch_list.append(symbol)
      self.watch_list.sort()
    

# removes a stock ticker symbol from the list

  def remove_ticker(self, symbol, my_list = False):
    if my_list == True:
      self.investment_list.remove(symbol)
    else:
      self.watch_list.remove(symbol)


# constructs the Yahoo Finance URL to pull stock data
# param is string of stock data to be pulled
  def construct_url (self, params, company_list):
    url = "http://download.finance.yahoo.com/d/filename?s="+company_list+"&f="+params+"&interval=1d&events=history&self.start_date, self.end_date, self.crumb"
    print("URL called")
    # response = urllib.request.urlopen(url)
    response = requests.get(url)

    data = csv.reader(io.TextIOWrapper(response))
    print("data populated")

    for row in data:
      try:
        print(row)
        self.stock_name.append(row[0])
        self.stock_price.append(float(row[1]))
        self.date.append(row[2])
        self.time.append(row[3])
        self.percent_change.append(float(row[4]))
        self.open.append(float(row[5]))
        self.high.append(float(row[6]))
        self.low.append(float(row[7]))
    
      except ValueError:
        pass
        return -0.1

  def build_stock_data(self):
    for i in range( len(self.watch_list)):
      self.stock_data = {'name': self.stock_name[i], 'price': self.stock_price[i],
      'date': self.date[i], 'time': self.time[i],
      'change': self.percent_change[i], 'open': self.open[i],
      'high': self.high[i], 'low': self.low[i]}
      
      self.stocks.update({self.watch_list[i]: self.stock_data})
      
    print("Stocks \n")
    print(self.stocks)
    
    #print(self.stocks["AAPL"]["time"]) 
    
  def write_JSON(self):
    with open('stockPrices.json', 'w') as f:
      json.dump(self.stocks, f)
      
      
