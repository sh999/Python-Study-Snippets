'''
Task:
Write a function that averages the indeterminate number of inputs
Reference:
Python cookbook
'''

def ave(firstNumber, *restOfNumbers):	# restOfNumbers is treated as a tuple
	average = (firstNumber + sum(restOfNumbers))/(1 + len(restOfNumbers))
	return average

print ave(1, 2, 3, 8, 9)