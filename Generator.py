'''
Generator.py
Practice for generators
http://anandology.com/python-practice-book/iterators.html
'''
def yrange(n):
	i = 0
	while i < n:
		yield i # generators use yield instead of return
		i += 1
y = yrange(3)
print y.next()
print y.next()
print y.next()
