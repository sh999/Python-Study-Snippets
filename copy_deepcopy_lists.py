'''
copy-deepcopy lists.py
Study of the different methods to copy lists
Tasks:
======

Simple copy list
	Create a list
	Create another list, equaling the above
	Print both lists
	Change an element in list 2; what happened to list 1?
Better copy:
	Copy a list from existing list where changing the second list won't affect the first

Reference:
http://www.python-course.eu/deep_copy.php

Todo:
complete tutorial from reference
'''
def printLists(list1, list2):
	print "List 1 =",list1
	print "List 2 =",list2


def copyList1():
	print "\nCopy list method 1 by equating "
	list1 = [1, 2, 3]
	print "Copying list1 to list2"
	list2 = list1
	printLists(list1, list2)
	print "Changing list 2..."
	list2[0] = 99
	printLists(list1, list2)
	print "List 1 gets changed too"

def copyList2():
	print "\nCopy list method 1 by slicing "
	list1 = [1, 2, 3]
	print "Copying list1 to list2"
	list2 = list1[:]
	printLists(list1, list2)
	print "Changing list 2..."
	list2[0] = 99
	printLists(list1, list2)
	print "List 1 stays intact"
copyList1()
copyList2()