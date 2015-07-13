'''
Tasks:
Create a class that has multiple inheritance
Show an example of method resolution order
'''
class A(object):
	def method1(self):
		print "Class A Method 1"
class B(A):
	def method1(self):
		print "Class B Method 1"
class C(A):
	def method1(self):
		print "Class C Method 1"
class D(C, B):
	pass

d = D()
d.method1()
print D.__mro__