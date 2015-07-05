'''
Tasks:
Create two sets A and B that has numbers, and make B a frozen set
	What's a frozen set?
Use set methods to create new sets that contain items...
	That are in A, but not B
	That are in B, but not A
	That are intersection of A and B
	That are union of A and B
'''
a = set([1,2,3,9])
b = frozenset([3,5,9,13])	# A frozen set is immutable, regular set mutable
print "Set A = ", a
print "Set B = ", b
print "In A, not in B = ", a.difference(b)
print "In B, not in A = ", b.difference(a)
print "Shared exclusively by A and B = ", a.intersection(b)
print "All in A and B = ", a.union(b)