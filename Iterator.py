'''
Iterator 2.py
'''

str = "formidable"

for i in str: # String objects can be for-looped, so it is an iterable
   print i,

print

it = iter(str)

print it.next()
print it.next()
print it.next()

print list(it)