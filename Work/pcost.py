# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    f = open(filename, 'rt')
    next(f) # skip headers
    cost = 0
    for line in f:
        # convert line to list
        row =  line.split(',')
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

