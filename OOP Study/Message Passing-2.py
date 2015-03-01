'''
Descended from Message Passing.py
Testing idea of a wrapper object

Two objects are contained into a wrapper object
Wrapper object can manipulate the two objects
The two objects don't know each other and never calls each other's function
'''
class Wrapper: 
	def __init__(self, obj1, obj2):
		self.obj1 = obj1
		self.obj2 = obj2
	
	def transferStatus(self): # Sets obj2's status to obj1's.  Wrapper only causes this behavior if manually told to by calling activate()
		status1 = self.obj1.getStatus()
		status2 = self.obj2.getStatus()
		if status1 == True:
			self.obj2.setTrue()
		else:
			self.obj2.setFalse()

class Bit:
	def __init__(self, name):
		self.status = False
		self.name = name
		
	def setTrue(self):
		self.status = True
	
	def setFalse(self):
		self.status = False

	def getStatus(self):
		return self.status

	def printStatus(self):
		print self.name, " = ", self.status

def main():
	# Create 2 objects and their wrapper
	bit1 = Bit("bit1")
	bit2 = Bit("bit2")
	wrapper = Wrapper(bit1, bit2)
	
	# Display initial statuses of the 2 objects (False by default)
	print "Initial values"
	bit1.printStatus()
	bit2.printStatus()

	print "\nValue after bit1 is changed"
	bit1.setTrue()
	bit1.printStatus()
	bit2.printStatus()
	print "Wrapper does nothing yet\n"

	wrapper.transferStatus()
	bit1.printStatus()
	bit2.printStatus()
	print "Wrapper has done its job"
	
main()


		