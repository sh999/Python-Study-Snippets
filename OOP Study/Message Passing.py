'''
Create two objects, event and target.
Event sends a message to target to change a variable in target
Remember to adhere to encapsulation and information hiding

todo:
Currently, event instance is created with argument of the target object that will be changed
Expand so that a container object contains both event and target and decide if this is a better construct
'''

class Event:
	def __init__(self, interactor):
		self.situation = False
		self.interactor = interactor
	def turnOn(self):
		self.situation = True
		print "Event turned on"
	def update(self):
		if self.situation:
			print "Event happened, initiating change"
			self.move()
		else:
			print "Event did not happen"
	def move(self):
		self.interactor.move()

class Target:
	def __init__(self):
		self.x = 0;
	def update(self):
		print "X = ", self.x
	def move(self):
		self.x += 1

def main():
	target1 = Target()
	event1 = Event(target1)
	event1.turnOn()
	event1.update()
	target1.update()

main()


		