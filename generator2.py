'''
Task:
Create a very simple generator, where the generator gives 3 different values; don't use a loop
Print out the values one by one
What happens when you exceed the number of values there are?
'''
def simpleGenerator():
	yield 1
	yield 2
	yield 3

g = simpleGenerator()
print g.next()
print g.next()
print g.next()
print a.next()	# Error because there are no more values to be yielded