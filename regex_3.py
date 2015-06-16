'''
Exercise to study regex
Task: Use regex to detect if a string has two consecutive vowels
Create various test strings
For each string, print if there's a match or not
Print the actual matched consecutive vowels in each string
'''
import re
string1 = "Elephant"
string2 = "Bayou"
string3 = "Breathed"
string4 = "Aegis"
string5 = "Biologia"
strings = [string1, string2, string3, string4, string5]

patternToMatch = "[aiueoAIUEO][aiueoAIUEO]"
for i in strings:
	print "Checking string: ", i
	if re.search(patternToMatch, i) != None:
		print "Found match", re.findall(patternToMatch, i)
	else:
		print "No match"
	print "-"*5
