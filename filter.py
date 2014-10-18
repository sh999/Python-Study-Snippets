'''
filter.py
Create a list of numbers
Create a new list using filter that has elements of above list that is filtered by a function
'''
def checkOver9000(a):
	if a > 9000:
		return True
	return False
a = [x for x in range(10000)]
over9000 = filter(checkOver9000,a)
print "a =",a
print "over9000 =",over9000