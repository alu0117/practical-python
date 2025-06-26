# pcost.py
#
# Exercise 1.27
import csv
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

path = 'Data/portfolio.csv'
total_cost = portfolio_cost(path)

print('Total cost', total_cost)

