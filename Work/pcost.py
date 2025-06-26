# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    next(rows) # skip headers
    cost = 0
    for row in rows:
        # extract number of shares
        try:
            shares = int(row[1])
            #extract price
            price = float(row[2])
        except ValueError:
            print("Warning: Missing Field")
        total = shares*price
        cost += total
    f.close()
    return cost

path = ''
if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = 'Data/portfolio.csv'
total_cost = portfolio_cost(path)

print('Total cost', total_cost)

