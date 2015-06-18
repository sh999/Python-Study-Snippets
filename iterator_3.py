'''
iterator_3
1)	Create an iterable
2)	Create two different iterators on this iterable
3)	Iterate through the different iterators separately--How is this done?
4)	What happens when you do this?
'''

a = [1,2,4,4,5,99]	# 1) A list is an iterable
b = iter(a)	# 2) iter(obj) returns/creates an iterator
print b
c = iter(a) # Multiple iterators can be created based on one given iterable
print next(b)	# 3) Iterating is done by calling next on an iterator
next(c)
next(c)
next(c)
next(c)
print next(c)	# 4) Since two different iterators are created from the same iterable, next() returns different values