'''inheritance-2 method resolution.py
Tasks:
======
Create class A and B
Create class C, which inherits from A then B
Define a function with the same name in A, B classes but which will yield different results
Define the same function in C, but call the one from A or B

To do:
Figure out why this calls B instead of A
'''

class A(object):
	def func(self):
		print "Printing A"
class B(object):
	def func(self):
		print "Printing B"
class C(A, B):
	def func(self):
		super(A,self).func()
a = A()
b = B()
c = C()
c.func()