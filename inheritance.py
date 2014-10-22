'''
inheritance.py
Inheritance study
Create class C, which inherits from class B, which inheriths from class A
Reference:
Python Essential Reference (3rd)
Tasks:
Implement multiple inheritance
'''
class A:
	def printMe(self):
		print "Class A printed"
class B(A):
	def printMe(self):
		print "Class B printed"
class C(B):
	def printMe2(self):
		print "Class C printed"
a = A()
b = B()
c = C()
print "Printing class A..."
a.printMe()
print "Printing class B..."
b.printMe()
print "Printing class C..."
c.printMe()

