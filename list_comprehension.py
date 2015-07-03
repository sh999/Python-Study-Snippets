'''
Task:
Create a list of integers
Use list comprehension to create lists based on the above list
	Make a list that takes all values of the first list, doubled
	Make a list that has all the odd numbers from the first list (hint: use a conditional)
Make a list that has all odd numbers from 1-1000
'''

firstList = [1,2,3,4,5]
doubled = [n*2 for n in firstList]
oddOnly = [n for n in firstList if n%2 != 0]
oddToThousand = [n for n in range(0,1000) if n%2 != 0]
print doubled
print oddOnly
print oddToThousand