'''
function arguments.py
Tasks:
======
Pass keyword arguments in a function call using an identifier
Pass keyword arguments using values in a dictionary
'''
def fraction(numerator, denominator):
	return numerator/denominator

print "Using identifiers..."
print fraction(numerator=3.0, denominator=12.0)
print "Passing dictionary values..."
print fraction(**{'numerator':3.0, 'denominator':12.0})
