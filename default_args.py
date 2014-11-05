'''
default_args.py

Task:
=====
Utilize default keywords for a function with an immutable type (number, string, etc.)
Utilize default keywords with a mutable object (e.g. list, dictionary, etc.)
	For example, define a function with an empty list and 
	What's the difference?
Reference:
https://docs.python.org/2/tutorial/controlflow.html#default-argument-values

'''
def printInfo(name, species="human"):
	print "Your name is",name
	print "You are a",species

def addMember(member, tribe=[]):
	print "tribe before appending",tribe
	tribe.append(member)
	return tribe

printInfo("Bob")
print addMember("Jack")
print addMember("Lucy")
print addMember("Lala") # The default keyword of empty list is executed int he first function call and not latter, so list keeps growing




