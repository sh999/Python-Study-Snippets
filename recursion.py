'''
recursion.py
Task:
=====
Implement a recursive function that solves a factorial

Reference:
==========
http://www.python-course.eu/recursive_functions.php
'''
def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial (n-1)

print factorial(4)