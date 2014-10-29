'''
class_repr_attr.py
Class representation and attibutes study
'''
class User:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return "This is a User class"

user = User("Gary")
print user