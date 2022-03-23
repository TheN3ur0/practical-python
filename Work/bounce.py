# !/usr/bin/env python3
# bounce.py
#
# Exercise 1.5


height = 100 #Meters 
amount = 0

x = 9

for i in range(x+1):
    amount = amount + 1
    height = height * 0.60
    print(amount, round(height, 4))
