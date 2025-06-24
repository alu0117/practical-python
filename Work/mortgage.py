# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months  = 342
month = 1

while month <= 342:
    principal = principal*(1+rate/12)-payment
    if month <= 12:
        principal = principal - (payment + 1000)
        total_paid = total_paid + (payment+1000)
    else:
        total_paid = total_paid + payment
    month += 1

print('Total paid', total_paid)

