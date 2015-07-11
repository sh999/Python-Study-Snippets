'''
A study on ways to loop
Tasks:
1) Loop a list of items, print the items and their indices
2) Create two lists of strings, loop simultaneously and print the items
3) Create a list of numbers in ascending order and loop over it in reverse
'''
for i, j in enumerate(["A", "B", "C"]):	# 1)
	print i, j

names = ["Alice", "Bob", "Chris"]	# 2)
numbers = ["111-2231", "392-1102", "392-2223"]
for name, phone in zip(names, numbers):
	print "Name = ", name, "\tPhone = ", phone
a = xrange(0, 10)

for i in reversed(a):	# 3)
	print i