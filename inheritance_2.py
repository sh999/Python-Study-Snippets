'''
inheritance_2.py
Testing mixins
unfinished
'''

class Person:
	def __init__(self, name):
		self.name = name
	def name():
		return self.name

class Runner:
	def __init__(self):
		pass
	def run(self):
		print "running"

class Jumper:
	def __init__(self):
		pass
	def jump(self):
		print "jumping"

class Athlete(Jumper, Runner, Person):
	def __init__(self):
		pass
	

def main():
	bob = Athlete()

main()