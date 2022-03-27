# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):

    with open (filename, 'rt') as f:

        rows = csv.reader(f)

        headers = next(rows)

        totalRow = 0
        sumTotal = 0

        for row in rows:

            try:
                totalRow = int(row[1]) * float(row[2])

                sumTotal = sumTotal + totalRow
            
            except ValueError:
                print("Couldn't parse", line)
    
        return round(sumTotal, 2)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost = portfolio_cost('Data/portfolio.csv')

print("Total cost is", cost)
       



