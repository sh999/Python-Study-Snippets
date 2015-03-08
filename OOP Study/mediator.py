'''
mediator.py
Goal:  Show an implementation of the mediator design pattern in python
References:
http://www.codeproject.com/Articles/455228/Design-Patterns-of-Behavioral-Design-Patterns
todo: Complete communication between aircraft and traffic control (register and check collision)
'''

# Aircraft class
class Aircraft:
	def __init__(self, planeID, altitude, controller):
		self.altitude = altitude
		self.controller = controller
		self.planeID = planeID
		self.controller.registerAircraft(self.planeID)

	def setAltitude(self, altitude):
		self.altitude = altitude

	def getAltitude(self):
		return self.altitude

	def changeAltitude(self, change):
		self.altitude = self.altitude + change
		self.controller.checkCollisions()

class TrafficCtrl:
	def __init__(self):
		pass
	def registerAircraft(self, planeID):

	def checkCollisions(self):
		pass

		

def main():
	trafficCtrl = TrafficCtrl()
	boeing747 = Aircraft("1", 1000, trafficCtrl) # Parameters: Aircraft ID, starting altitude, traffic controller
	airbus380 = Aircraft("2", 2000, trafficCtrl)
	cessna172 = Aircraft("3", 1500, trafficCtrl)
	boeing747.changeAltitude(900)

main()

