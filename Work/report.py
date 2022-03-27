# report.py
#
# Exercise 2.4

import csv
from pprint import pprint


def read_portfolio(filename):
    
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
          
            holding = {
                    "name":row[0],
                    "shares":int(row[1]),
                    "price":float(row[2])
                }

            portfolio.append(holding)

        return portfolio


def read_prices(filename):

    d = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        try:
            for row in rows:

                d[row[0]] = float(row[1])

        except IndexError:
            row = None
        

        return d


def check_unique():
    
    stockList = []
    uniqueStocks = []

    portfolio = read_portfolio('Data/portfolio.csv')
    
    for x in portfolio:

        stockList.append(x['name'])
        stockNames = set(stockList)
    
    for y in stockNames:
        uniqueStocks.append(y)

    return uniqueStocks

#Stocknames, met de prijs en aantal

#Huidige prijs van aandeel van stocks die in de portfolio zitten
prices = read_prices('Data/prices.csv')

#for y in prices:

uniqueStocks = check_unique()
