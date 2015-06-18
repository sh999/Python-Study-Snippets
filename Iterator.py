'''
Iterator 2.py

1) Are strings iterators or iterables?
2) How do you create an iterator?
'''

str = "Hello"

for i in str: # String objects can be iterated through for, therefore it's an iterable. 
   print i,	  # An iterable is NOT an iterator...
print

it = iter(str) # This creates an iterator from the string by returning an iterator object

print it.next() # Iterator object has next method
print it.next()
print it.next()
