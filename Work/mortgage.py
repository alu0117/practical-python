# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months  = 342
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while month <= months:
    principal = principal*(1+rate/12)
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - (payment + extra_payment)
        if principal < 0:
            break
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal - payment
        if principal < 0:
            break
        total_paid = total_paid + payment
   
    print(month, round(total_paid,2), round(principal,2))
    month += 1

print('Total paid', round(total_paid,2))

