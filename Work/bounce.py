# bounce.py
#
# Exercise 1.5
n_bounces = 10
bounce = 1
h = 100
while bounce <=10:
    h = round((3/5)*h,4)
    print(bounce, h)
    bounce += 1

