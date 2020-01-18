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
      self.watch_list.sort()
    else:
      self.watch_list.append(symbol)
      self.watch_list.sort()
    

# removes a stock ticker symbol from the list
  def remove_ticker(self, symbol, my_list = False):
    if my_list == True:
      self.investment_list.remove(symbol)
    else:
      self.watch_list.remove(symbol)

  def build_stock_data(self):
    for ticker in len(self.watch_list):
      self.stock_data = {'name': self.stock_name[ticker], 'price': self.stock_price[ticker],
      'date': self.date[ticker], 'time': self.time[ticker],
      'change': self.percent_change[ticker], 'open': self.open[ticker],
      'high': self.high[ticker], 'low': self.low[ticker]}

      self.stocks.update({self.watch_list[ticker]: self.stock_data})

    print("Stocks \n")
    print(self.stocks)

    #print(self.stocks["AAPL"]["time"]) 

  def write_JSON(self):
    with open('stockPrices.json', 'w') as f:
      json.dump(self.stocks, f)

