# report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            portfolio.append({'name':row[0], 'shares': int(row[1]),'price': float(row[2])})
    return portfolio

def read_prices(filename):
    d = {}
    f = open(filename, 'rt')
    rows = csv.reader(f)
    for row in rows:
        try:
            d[row[0]] = float(row[1])
        except IndexError:
            print('Row is empty')
    f.close()
    return d
    
def current_value(portfolio, stocks):
    value = 0
    change = 0
    for holding in portfolio:
        stock_name = holding['name']
        cur_price = stocks[stock_name]
        value += holding['shares'] * cur_price

        # Calculate gains/loss
        change += (cur_price - holding['price']) * holding['shares']
    return value, change
