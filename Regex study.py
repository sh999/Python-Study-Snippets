'''
Regex study.py

Tasks:
======
Define a pattern object
Define a match object by comparing a string to the pattern object
Print the matched string

References:
===========
https://docs.python.org/2/howto/regex.html
'''
import re

def matching():
	patternObj = re.compile('[a-z]+') # Creates Pattern object
	matchObj = patternObj.match('hello') # Creates Match object
	print "Pattern object =",patternObj
	print "Match object =",matchObj
	matchObj.group()
	print "Matched string =",matchObj.group()

matching()