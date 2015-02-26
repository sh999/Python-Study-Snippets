'''
stacks.py
Task:
Implement basic stack using array

eg
s = Stack()
print s --> [None]
s.push(2)
print s --> [2]
s.push(99)
print s --> [99, 2]
s.pop()
print s --> [2]

'''

class Stack:
	def __init__(self):
		self.stack = [0]*10
		self.topPosition = 0
	def __str__(self):
		return str(self.stack)

	def push(self, x):
		self.stack[self.topPosition] = x
		self.topPosition += 1
	def pop(self):
		self.stack[self.topPosition-1] = 0
		self.topPosition -= 1

def main():
	s = Stack()
	print s
	s.push(2)
	print s
	s.push(99)
	print s	
	s.push(213)
	print s
	s.pop()
	print s
	s.pop()
	print s
	s.pop()
	print s
	
main()

