'''
dictionary_sort.py
Task:
====
Given a list of dictionaries, sort the dictionaries by one of the keys
Hint: Use the operator module
'''
from operator import itemgetter
rows = [{'itemname':'chips', 'cost':3},
		{'itemname':'burrito', 'cost':8},
		{'itemname':'car', 'cost':10000}]
sortedRows = sorted(rows, key=itemgetter('itemname'))
print sortedRows