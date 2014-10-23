'''
inheritance.py
Inheritance study

Tasks:
======
- Create class C, which inherits from class B, which inherits from class A
- Define a function in A that doesn't exist in B, and execute that function for both A and B
	What happens?
- Show that a function in C can override a function in A
- Use super() in C
	What does it do?

References:
==========
- Python Essential Reference (3rd)
- http://learnpythonthehardway.org/book/ex44.html

'''
class A(object):
	def printMe(self):
		print "Class A printed"
class B(A):
	pass
class C(B):
	def printMe(self):
		print "Class C printed"
		super(C, self).printMe() # Calls the function in its super class
a = A()
b = B()
c = C()

print "Printing class A..."
a.printMe()
print "Printing class B..."
b.printMe() # Since function is not in B, the one in its parent is called
print "Printing class C..."
c.printMe() # Function in c overrides one in A


