'''
radio-button.py
Goal:  Add button class to base radio.py
'''
class Radio():
	def __init__(self):
		self.powerButton = PowerButton()
	def dispStatus(self):
		print "Radio is on? ", self.powered
	def turnOn(self):
		powerButton.switchOn()
		print "Radio turned on"
	def turnOff(self):
		powerButton.switchOn()
		print "Radio turned on"
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

class PowerButton:
	def __init__(self):
		self.power = "off"
	def switchOn(self):
		self.power = "on"
	def switchOff(self):
		self.power = "off"

def main():
	radio = Radio()
	radio.dispStatus()


main()



