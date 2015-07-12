'''
Study on doctest, a way to test programs based on documentation string
'''

def isEven(x):
	'''
	>>> 
	'''

	if x % 2 == 0:
		return True
	else:
		return False

def _test():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	_test()