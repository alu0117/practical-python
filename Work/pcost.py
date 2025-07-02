# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows) # skip headers
    cost = 0
    for row_n, row in enumerate(rows, start = 1):
        record = dict(zip(headers, row))
        # extract number of shares
        try:
            shares = int(record['shares'])
            #extract price
            price = float(record['price'])
            total = shares*price
            cost += total
        except ValueError:
            print(f"Row {row_n}: Couldn\'t convert: {row}")
    f.close()
    return cost

def main(arguements):
    path = ''
    if len(arguements) == 2:
        path = arguements[1]
    else:
        path = 'Data/portfolio.csv'
    total_cost = portfolio_cost(path)
    print('Total cost', total_cost)

if __name__=='__main__':
    main(sys.argv)