'''
recursion-2.py
Tasks:
======
Implement simple recursive function to calculate
	nth fibonacci number
Implement the same but with memoization
	Why is this better?
Reference:
==========
http://www.python-course.eu/recursive_functions.php
'''


def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

memo = {0:0, 1:1} # memoization saves recursion results in a dictionary
def fibm(n):
	if not n in memo:
		memo[n] = fibm(n-1) + fibm(n-2)
	return memo[n]

print fib(10)
print fibm(10)