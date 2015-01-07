'''
String representation
Objective: 
==========
Learn what str() and repr() do
Use these to output string in an organized way
Tasks:
======
Store a string variable
	Print variable as it's converted by str() and repr()
	What's the difference in output?
Print a str(x) and repr(x) where x is a ratio of two floating numbers
	What's the difference in output?
Print a table of numbers with these requirements:
	On the leftmost column, print 1-10 
	On the middle column, print the number X 2
	On the rightmost column, print the number X 3
	Columns should align
Source:
=======
https://docs.python.org/2/tutorial/inputoutput.html#fancier-output-formatting
'''

s = 'Hey man'
print str(s)
print repr(s) # Results in quotation around output
print str(22.0/7.0)
print repr(22.0/7.0) # More digits are output
for x in range(1, 11):
	print repr(x).rjust(2), repr(x*2).rjust(3),
	print repr(x*3).rjust(4)
