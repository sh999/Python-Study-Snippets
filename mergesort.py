'''
mergesort.py
Goal:  Implement my own mergesort
See reference, figure 10
Try to implement the algorithm without looking at the site
Use figure as guide as it describes step by step what the algorithm should do
Reference:
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

Steps:
Split list until it has 1 element
Merge adjacent elements

todo:
make algorithm that does merging of n > 1 elements
	comparison between 2 elements works, make it loopable so it can do n > 1 element merges
'''

toSort = [54, 26, 93, 17, 77, 31, 44, 55, 20]

def merge(list1, list2):
	reference = list1[0]
	subject = list2[0]	# Subject is compared to reference and placed left or right in merged list depending if it is bigger or smaller
	mergedList = []
	refPosition = 0
	mergedList.append(reference)	# Add first element, the first reference
	
	print "Merging list 1 = ", list1, " and list 2 = ", list2
	print "Reference = ", reference
	print "Subject = ", subject
	print "Merged list = ", mergedList

	leftOfRef = len(mergedList) - 1 # Position left of reference, used below
	if subject < reference: # Insert subject to left or right of reference depending if it's smaller or larger
		mergedList.insert(leftOfRef, subject)
	else:
		mergedList.append(subject)
		refPosition += 1
		reference = mergedList[refPosition]

	print "New merged list = ", mergedList
	print "New position = ", refPosition
	print "New reference = ", reference

def main():
	pass

def testMerge():
	list1 = [1, 8]
	list2 = [4, 7]
	merge(list1, list2)

def insertLeft():	# Testing insertion of an element into the next to last element of list
	a = [1, 2, 3, 4]
	a.insert(len(a)-1, 'a')
	print a

testMerge()
