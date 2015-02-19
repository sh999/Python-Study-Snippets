'''
Regex study.py

Tasks:
======
Define a pattern object
Define a match object by comparing a string to the pattern object
	There are at least two main ways to create a match object
	Do both; what is the difference between them?
Print the matched string

References:
===========
https://docs.python.org/2/howto/regex.html
'''
import re

def createMatch():
	patternObj = re.compile('h\w*') # Creates Pattern object
	matchObj = patternObj.match('haha') # Creates Match object using match()
	# matchObj2 = patternObj.search('grey') # Match object using search()
	matchObj.group()
	print "Matched string =",matchObj.group() # Match searches match from beginning of pattern
	# print "Matched string2 =",matchObj2.group() # search() searches match inside pattern
	print matchObj.end()
createMatch()