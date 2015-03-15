'''
static_class_methods.py
Task:
Create a class that has a static and class method
	Describe static and class method
Reference:
'''

class A:
	x = 99
	@staticmethod
	def aStaticMethod(x):	# A static method is associated with a class, not any instance
		print "x is", x
	@classmethod
	def aClassMethod(cls):	# A class method passes the class itself (cls is a parameter for the class; cls is they convention, but it can be anything)
		print cls.x

A.aStaticMethod(5)	# 'x is 5'
A.aClassMethod()	# 99
