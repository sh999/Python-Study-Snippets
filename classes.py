'''
Tasks:
Create an Animal class with a class variable status
	Set status to "Alive"
Why do object methods have self as arguments?
Create a static method and a class method
	What are they?  What are the differences?
'''

class Animal(object):
	status = "Alive"
	@staticmethod	# Static methods are for all instances of the class
	def bla():
		print "Running static method"
	@classmethod	# Class methods are similar to static methods, but passes the class itself as argument
	def printClass(cls):
		print cls
	def __init__(self, name):	# Object methods take the object itself, which is why self is an argument
		print "Creating animal"
		self.name = name
	def printName(self):
		print "Animal name = ", self.name

a = Animal("Lion")
a.printName()
print a.printName
print a.status
a.bla()
a.printClass()