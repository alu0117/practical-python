# pcost.py
#
# Exercise 1.27
path = 'Data/portfolio.csv'
f = open(path, 'rt')
headers = next(f) # skip headers
cost = 0
for line in f:
    # convert line to list
    row =  line.split(',')
    # extract number of shares
    shares = int(row[1])
    #extract price
    price = float(row[2])
    total = shares*price
    cost += total
print('Total cost', cost)
f.close()