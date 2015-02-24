'''
Recursion-3
Task: Use simple recursion to decrement a value from 5 to 1
1-Define base case of a recursion function and identify the base case here
2-Why is a base case necessary?

References:
http://cscircles.cemc.uwaterloo.ca/16-recursion/
'''
def decrement(n):
	if n == 0:  # 1-Base case is part of function where it doesn't call itself
		print "End decrement" #2-Base case is needed in every recursion function so that it eventually terminates
	else:
		print(n)
		decrement(n-1)
decrement(5)

