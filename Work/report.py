# report.py
#
# Exercise 2.4
import csv
import sys
import fileparse
def read_portfolio(filename):
    portfolio = None

    with open(filename, 'rt') as f:
        portfolio = fileparse.parse_csv(f, types=[str, int, float])
    return portfolio

def read_prices(filename):
    with open(filename, 'rt') as f:
        price_list = fileparse.parse_csv(f, types = [str,float], has_headers = False)
    d = dict(price_list)
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
    if len(arguements) != 3:
        raise SystemExit(f'Usage: {arguements[0]} ' 'portfolio pricefile')
    portfile = arguements[1]
    pricefile = arguements[2]
    portfolio_report(portfile, pricefile)

if __name__=='__main__':
    #main(sys.argv)
    main(['report.py', 'Data/portfolio.csv','Data/prices.csv'])