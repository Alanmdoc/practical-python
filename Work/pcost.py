# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
	total_cost = 0.0
	with open(filename, 'rt') as file:
		rows = csv.reader(file)
		headers = next(rows)
		for rowno, row in enumerate(rows, start=1):
			record = dict(zip(headers, row))
			try:
				nshares = int(record['shares'])
				price = float(record['price'])
				total_cost += nshares * price
			except ValueError:
				print(f'Rows {rowno}: Bad row: {row}')
				continue
			'''try:
				prices = float(row[2].rstrip())
			except ValueError:
				print(f'Row {rowno}: Bad row: {row}')
				continue
			total_cost += shares * prices'''
		return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
	print("File name (e.g Data/filename.csv): ")
	filename = input()

cost = portfolio_cost(filename)

print("Total cost", cost)