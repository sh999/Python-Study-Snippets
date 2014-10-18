'''
Regex study.py
Reference:

Objective:
Display all meta/control characters
'''
import re

print "Metacharacters = ( + ? . * ^ $ () [] {} | \\"
reference = "My name is Tom"
str = 'an example word:cat!!'

match = re.search(r'word:www', str)

# If-statement after search() tests if it succeeded
if match:                      
	print 'found', match.group() ## 'found word:cat'

else:
	print 'did not find'