'''
radio.py
Goal:  Build simple radio to experiment with Object Oriented Design
Current Status:  Made basic skeleton radio class 
Todo:  Make another class to interact or a subclass
	   i.e. make a station selector class or volume knob class
'''
class Radio():
	def __init__(self):
		self.powered = False
	def dispStatus(self):
		print "Radio is on? ", self.powered
	def turnOn(self):
		self.powered = True
		print "Radio turned on"
	def turnOff(self):
		self.powered = False
		print "Radio turned off"
	def playMusicStation(self):
		if self.powered is True:
			print "Playing music station"
		else:
			print "Can't play music station, turn on radio first"
	def playCD(self):
		if self.powered is True:
			print "Playing CD"
		else:
			print "Can't play CD, turn on radio first"

def main():
	radio = Radio()
	radio.dispStatus()
	radio.dispStatus()
	radio.playCD()
	radio.turnOn()
	radio.playCD()
	radio.turnOff()
	radio.playCD()

main()



