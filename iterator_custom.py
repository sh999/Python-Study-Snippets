'''
iterator_custom.py
Task
====
Create a class that is an iterator object
What is the characteristic of an iterator?
Print values of an iterator using a for loop
	What is the relationship between a for loop and an iterator?
'''
class CustomIterator:
	def __init__(self, data):
		self.data = data
		self.index = -1
	def __iter__(self):
		return self
	def next(self):	# Iterators must have a next()
		if(self.index == len(self.data)-1):
			raise StopIteration
		self.index = self.index + 1
		return self.data[self.index]
		

myIterator = CustomIterator('hello')
for i in myIterator:	# A for loop that works on an iterator essentially calls the iterator's next() each time it loops
	print i
