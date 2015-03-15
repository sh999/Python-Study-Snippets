'''
introspection.py

Task:
Create two classes and instances for each
Check if one of the objects is an instance of one of the classes

Reference:
Alchi, Pro Python, pg 117
'''

class Class1:
	def __init__(self):
		pass
class Class2:
	def __init__(self):
		pass

def main():
	obj1 = Class1()
	obj2 = Class2()
	print isinstance(obj1, Class1)	# Checks if obj1 is an instance of Class1. Returns True or False
	print isinstance(obj2, Class1)	

main()

