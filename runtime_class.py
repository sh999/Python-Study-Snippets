'''
runtime_class.py
Create a class with one assigned integer using conventional class creation
Create another class with the same structure, but create it at runtime
Print the integer values to check if the program is correct

Reference:
Alchi, Pro Python, page 120
'''

class Class1:
	x = 5

obj1 = Class1()
print obj1.x

Class2 = type("Class2", (int,), {"x" : 6})	# Runtime class is created. The structure is equivalent to Class1; note the use of dictionary to assign x
obj2 = Class2()
print obj2.x	# 6



