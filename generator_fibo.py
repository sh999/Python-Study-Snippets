'''
Generator_fibonacci
Use a generator to output the fibonacci sequence given n, where n is the 
length of the sequence
1) What makes a generator unique?
2) What happens if you do: print aGenerator(x)?
3) What is the proper way to output result from the generator?

Reference:  Pro Python (Hetland)
'''
def fibonacciGenerator(x):
	a, b = -1, 1
	while x > 0:
		numSum = a + b
		yield numSum	# 1) Yield makes generators unique. It's like a return, but doesn't interrupt the function/generator

		a, b = b, numSum
		x -= 1

print fibonacciGenerator(5)	# 2) Doesn't work to output values. Will print that it's a generator; correct output below
for i in fibonacciGenerator(5):	# 3) A generator must be looped like this to print individual yielded values
	print i


