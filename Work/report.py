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

def make_report(port, cur_prices):
    holdings = []
    for p in port:
        buy_price = p['price']
        cur_price = cur_prices[p['name']]
        change = cur_price-buy_price
        tup  = (p['name'], p['shares'], cur_price, change)
        holdings.append(tup)
    return holdings

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

def format_header(tup):
    for header in tup:
        print(f'{header:>10s}', end = ' ')
    print()
    for _ in tup:
        print('-'*10, end=' ')
    print()

# Script begins here

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
format_header(headers)

for name, shares, price, change in report:
    formatted_price = f'${price:<.2f}'
    print(f'{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}')