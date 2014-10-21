'''
iterables and generators.py
Create an iterable
Create a generator
Iterate through each of the above
Iterate one more time
	What happens to the iterable and generator?
	Any differences?
'''

iterable = [1, 2, 3, 4, 5]
generator = (x for x in range(1,6))

print "First iteration"
print "Values in iterable:"
for i in iterable:
	print i
print "Values in generator:"
for i in generator:
	print i

print "Second iteration"
for i in iterable:
	print i
print "Values in generator:"
for i in generator:
	print i # Will not print from 1 to 5 because generator is "done"


