'''
sorting.py
Exploring simple python sorting methods

Objectives:
===========
Sort a list using two different built-in methods and describe the difference
Given a list [['string1', value1], ['string2', value2]...['stringN', valueN]
	sort the string by value using one line

References:
===========
https://docs.python.org/2/howto/sorting.html
'''
class Student:
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade
	def __repr__(self):
		return repr((self.name, self.grade))

a = [1,3,2,5,0]
b = [10,30,11,2]
print sorted(a)
b.sort() # only works for lists; changes original list
print b

grades = [('Bob', 99), ('Tim', 77), ('Tom', 100)]
print sorted(grades, key=lambda student: student[1]) # Sorts names by associated grades

studentObjects = [Student('Mike', 78), Student('Ann', 99), Student('Lee', 77)]
print sorted(studentObjects, key=lambda student: student.grade) # Same as above but shows use on objects