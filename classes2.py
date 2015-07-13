'''
Some more experiments on classes
Tasks:
'''

class President(object):
	def __init__(self, name, term):
		self.name = name
		self.term = term

	def printBio(self):
		self.bio = "President " + self.name + " is president #" + str(self.term)
		print self.bio

	def getMessage(self):
		return self.bio

class Rockstar(object):
	def __init__(self, name, band):
		self.name = name
		self.band = band
	
	def printBio(self):
		self.status = "Rock star " + self.name + " belongs to the band " + self.band
		print self.status

	def getMessage(self):
		return self.status

def showBio(person):
	print person.getMessage()


carter = President("Jimmy Carter", 39)
carter.printBio()
hendrix = Rockstar("Jimi Hendrix", "The Jimi Hendrix Experience")
hendrix.printBio()
print "-"*10
showBio(carter)
showBio(hendrix)
