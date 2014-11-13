'''
iterable_vs_iterator.py
References
==========
http://stackoverflow.com/questions/9884132/understanding-pythons-iterator-iterable-and-iteration-protocols-what-exact
'''
s = "hello"  # A string is an iterable 
# print(next(s)) # Does not work because next() only works on iterators
i = iter(s) # iter function returns an iterator, in this case i
print(next(i)) # Now this works because i is an iterator
print(next(i))
print(next(i)) # ...next() will return different value each time
print(next(i))
print(next(i))
print(next(i)) # next() runs out of things to print; string "ended" previously