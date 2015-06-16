'''
Defining traceback
1) What is a traceback and stack diagram, and how do they relate?
2) What's another name for it?
3) Demonstrate a traceback using nested functions
'''

# 1) A stack diagram can be used to illustrate which variables belong to which functions.
# 	 If there's a function that calls another function, and there's an error in the last
#	 function, the interpreter will output a traceback, which is a set of statements that
#	 trace where the error is starting from the outside function to the inside function
# 2) A synonym for traceback is stack trace
def func2(x):
	print x
	print z	# Z is undefined, so there will be an error and traceback report

def func1(x):
	func2(x)

func1(3)