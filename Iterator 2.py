'''
Iterator 2.py
Reference = http://anandology.com/python-practice-book/iterators.html
'''

class myIterator:
	def __init__(self, n):
		self.i = 0
		self.n = n
	def __iter__(self):
		return self
	def __next__(self):
		if self.i < self.n:
			i = self.i
			sel.i += 1
			return i
		else:
			raise StopIteration()

a = myIterator(5)
a.next() 