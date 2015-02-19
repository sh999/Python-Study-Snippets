'''
Regex2.py 

Tasks
=====
Create a regex that detects one to three consecutive 'M' characters
What does re.search() do?

References
==========
http://www.diveintopython.net/regular_expressions/
'''
import re
s = "Hello world, my name is Bill"
print 'Original string = ', s
print 'Modified string = ', s.replace('Bill', 'Bob')
print 'Modified with regex = ', re.sub('Bill', 'Bob', s) # First argument 'Bill' is the regex object
pattern = "^M?M?M?$"  
'''
Description of symbols above:
^M? : 0 to 1 M at the beginning of string
M? : 0 to 1 presence of M
M?$ : 0 1to 1 M at the end of string
'''
print(re.search(pattern, 'M'))
'''
re.search() tries to find the pattern in the string
If found, an object, but if no match, then it returns None
'''
print(re.search(pattern, 'MMM'))	# Returns an object id because of match
print(re.search(pattern, 'XXXXX'))	# Returns None because no match
