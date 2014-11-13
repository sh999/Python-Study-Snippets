'''
Iterator 2.py
'''

str = "Hello"

for i in str: # String objects can be iterated through for, therefore it's an iterable
   print i,

print

it = iter(str) # Returns an iterator object

print it.next() # Iterator object has next method
print it.next()
print it.next()

print list(it)