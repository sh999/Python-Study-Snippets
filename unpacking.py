'''
unpacking.py
Task
====
Demonstrate a simple "unpacking" of data
Show what happens when unpacking is done incorrectly (in terms of variable assignments)
'''

person = ("Alice", "F", 26, "433-2291")
name, gender, age, phone = person	# Each item in the tuple corresponds to a variable
print "Name = ", name
print "Gender = ", gender
print "Age = ", age
print "Phone number = ", phone
a, b, c, d, e = person	# The number of variables on the left side do not equal the number of items in the tuple, resulting in an error
