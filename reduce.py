'''
reduce.py

Create a list of numbers
Use reduce to return a sum of numbers in the list
'''
def sum(x, y):
	return x + y
a = [1,2,3,4]
result = reduce(sum, a)
print result
