'''
set.py
Tasks:
======
Create two sets of letters
Print simple set operations between the two
	e.g. find unique letters, shared letters, etc.

Reference:
==========
https://docs.python.org/2/tutorial/datastructures.html
'''
a = set('hello there')
b = set('my name is')
print a
print b
print a-b # letters in a, not b
print a&b # ..in a and b
print a^b # ..in a or b