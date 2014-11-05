'''
Generator.py
Practice for generators

Task:
=====

Create a simple generator function, one that gives 5 values
	What is the difference between a typical function and a generator?

Reference:
==========
http://anandology.com/python-practice-book/iterators.html
'''
def aGen():
	i = [1,2,3,4]
	for e in i:
		yield e

def myRange(n):
	counter = 0
	while counter < 10: # The counter limits loop to size of range
		yield counter # Difference: Generators use yield instead of return
					  # In effect, the looping creates a "list" of values from each loop's yielded value
		counter += 1

y = myRange(3)
print y.next()
print y.next()
print y.next()
