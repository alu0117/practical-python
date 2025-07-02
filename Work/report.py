# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers,row))
            portfolio.append({'name':record['name'], 'shares': int(record['shares']),'price': float(record['price'])})
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

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    format_header(headers)

    for name, shares, price, change in report:
        formatted_price = f'${price:<.2f}'
        print(f'{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    report = make_report(portfolio, prices)
    print_report(report)
            
def main(arguements):
    portfile = arguements[1]
    pricefile = arguements[2]
    portfolio_report(portfile, pricefile)

if __name__=='__main__':
    main(sys.argv)