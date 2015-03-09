'''
set_2.py
Goal:  Learn basic Set methods
Task:
Create a set of numbers 1-3
Add number 4 to the set
Add numbers 4 and 5 to the set
	What makes set unique compared to other sequence types after adding these values?
There are two ways to remove a value from Sets
	What is the difference between the two ways?
Remove an arbitrary element from the set
Remove all elements from the set
'''
a = {1, 2, 3}
a.add(4)
print a
a.update({4, 5})	# Sets contain unique values, so only 5 is added
print a
a.discard(6)	# Doesn't result in error if the value isn't in the set already
# a.remove(6)	# Results in error because 6 isn't in the set already
print a.pop()	# Removes an arbitrary element 
a.clear()
print a
