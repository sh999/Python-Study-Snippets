'''
lambda.py
Lambda function study
Create a list, a math function, and use map to change elements of that list using the function
Now do the same but with lambda
'''
def triple(a):
	return a * 3
a = [1,2,3,4,5]
print "a =",a
tripleOfA = map(triple, a)
print "tripleOfA =",tripleOfA
tripleofALambda = map(lambda x: 3 * x, a)
print "tripleofALambda =",tripleofALambda




