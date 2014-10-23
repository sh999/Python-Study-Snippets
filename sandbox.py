class A(object):
	def method(self):
		print "I am A"
class B(A):
	def method(self):
		print "I am B"
class C(B):
	def method2(self):
		print "I am C"

a = A()
b = B()
c = C()

a.method()
b.method()
c.method()