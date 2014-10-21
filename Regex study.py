'''
Regex study.py

Print all meta/control characters

References:
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