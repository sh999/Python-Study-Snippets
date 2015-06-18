'''
Iterator 2.py
Reference = http://anandology.com/python-practice-book/iterators.html
'''

class myIterator:
	def __init__(self, n):
		self.i = 0
		self.n = n
	def __iter__(self):	#	iter() always returns an iterator; you can return the object itself, like in here 
		return self
	def next(self):
		if self.i < self.n:
			i = self.i
			self.i += 1
			return i
		else:
			raise StopIteration()

a = myIterator(5)
# print a.next() 
print a