'''
map.py
Map function study
Covers the use of map, zip

Basic:
Create a list
Create a function that does a mathematical operation on a number
Use map to do this operation to elements of the list

Multiple maps:
Create two lists
Create a function that does operation on two lists
Use map to execute funciton on two lists

Merging lists:
Take two lists above and merge them using map
Use zip instead of map.  What's the difference?
'''
def double(x):
	return x*2
def square(x, y):
	return x*x, y*y

a = [1,2,3,4,5]
result = map(double,a)
print "a =",a,"\nmap(a) =",result

b = [1,2,3]
c = [7,8,9]
result2 = map(square,b,c)
print "\nb =",b,"and c=",c,"\nmap(b,c) =",result2
print "Merged b and c using map =",map(None,b,c)
print "Merged a and b using zip =",zip(a,b)
