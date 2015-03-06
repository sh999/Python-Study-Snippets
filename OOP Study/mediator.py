'''
mediator.py
Goal:  Show an implementation of the mediator design pattern in python
References:
http://www.codeproject.com/Articles/455228/Design-Patterns-of-Behavioral-Design-Patterns
'''

# Aircraft class
class Aircraft:
	def __init__(self):
		pass
	def setAltitude(self, altitude):
		self.altitude = altitude
	def getAltitude(self):
		return self.altitude
	def changeAltitude(self, change):
		self.altitude = self.altitude + change

class TrafficCtrl:
	def __init__(self):
		pass

def main():
	trafficCtrl = TrafficCtrl()
	boeing747 = Aircraft(1000, trafficCtrl)
	airbus380 = Aircraft(2000, trafficCtrl)
	cessna172 = Aircraft(1500, trafficCtrl)
	boeing747.changeAltitude(900)

main()

