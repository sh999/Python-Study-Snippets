'''
Play with built in exceptions
'''

a = [1, 2, 3, 3, 4, 1]
try:
	print a[6]
except IndexError:
	print "Out of bounds. Printing last element instead"
	print a[5]

try:
	print 33/0
except ZeroDivisionError:
	print "Don't divide by zero!"

try:
	print "Running function..."
	hahaha()
except NameError:
	print "That function or variable doesn't exist. Define it!"


