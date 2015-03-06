'''
unit_test.py
Goal:  Demonstrate basic unit testing
References:
http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html
'''

import unittest
def IsOdd(n):
	return n % 2 == 1 # Returns true if n is odd
class IsOddTests(unittest.TestCase):	
	'''
	This class contains all the cases we want to test, which is value 1 or 2
		This is an example of a text fixture, which is a class derived from unittest.TestCase that groups together test cases
	Each case is put in a class function below
	Each function uses functions from the unittest module
	'''
	def testOne(self):	# This is a test case
		self.failUnless(IsOdd(1))
	def testTwo(self):	# This is another test case
		self.failIf(IsOdd(2))
def main():
	unittest.main()
if __name__ == '__main__':
	main()