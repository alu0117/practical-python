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
    
