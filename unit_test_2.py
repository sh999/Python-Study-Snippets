'''
unit_test_2.py
Goal: Demonstrate unit testing with my own example 
	(unit_test.py shows example derived from a site)
Example:
	Create a function that checks if a DNA is valid
		It is valid if it contains the bases A, C, T, or G
		It is invalid if it contains anything other than the above
	Make unit tests that has two scenarios:  A known valid and invalid strings
'''
import unittest
def isDNASequenceValid(sequence):
	for i in sequence:
		print i
		if i != 'A' and i != 'C' and i != 'T' and i != 'G':
			print 'oy'
			return False
	return True

class DNASeqValidityTests(unittest.TestCase):
	def test1(self):
		self.failIf(isDNASequenceValid("TXTG"))
	def test2(self):
		self.failUnless(isDNASequenceValid("CCTG"))

def main():
	unittest.main()

if __name__ == '__main__':
	main()