'''
database.py
Task: 
Implement a simple database system
Ask user to enter name, age, and phone number of a person.  
The user will be associated with a numeric user ID.  
The user information will be inserted into the database.  
Have the capability to print out the database.

todo:
Modify so that adding a second user doesn't overwrite the information for the first user
	Currently, updating the dictionary erases the original information. Done 150317.
'''

class Database():
	def __init__(self):
		self.userDict = {}
		self.userList = []

	
	def insertItem(self, user):
		self.userList.append(user)
		# self.userList.append({"ID # = ":user.ID, "Name = ":user.name, "Age = ":user.age, "Phone # = ":user.phone})
	
	def deleteItem(self):
		pass

	def disp(self):
		print "ID \t Name \t Age \t Phone number"
		print "*"*35
		for user in self.userList:
			print user.ID, '\t', user.name, '\t', user.age, '\t', user.phone

class Person():
	ID = 0
	def __init__(self, name, age, phone):
		self.ID = Person.ID
		self.name = name
		self.age = age
		self.phone = phone
		Person.ID += 1

class IncrTest():
	x = 0
	def __init__(self):
		self.x = IncrTest.x
		print "setting up x =", self.x
		IncrTest.x += 1

def main():
	user1 = Person("Bob", 33, "123-4567")
	user2 = Person("Alice", 44, "222-2212")
	database = Database()
	database.insertItem(user1)
	database.insertItem(user2)
	database.disp()

main()
