# pcost.py
#
# Exercise 1.27
import csv
import sys
import report

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
    if len(arguements) != 2:
        raise SystemExit(f'Usage: {arguements[0]} ' 'portfile')
    path = arguements[1]
    total_cost = portfolio_cost(path)
    print('Total cost', total_cost)

if __name__=='__main__':
    main(sys.argv)