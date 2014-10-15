'''
Iterator 2.py
'''

str = "formidable"

for i in str:
   print i,

print

it = iter(str)

print it.next()
print it.next()
print it.next()

print list(it)