'''
numpy study.py
Use numpy
Create array, reshape it, describe its length and shape.

'''
from numpy import *
a = arange(10)
print "Linear array = \n", a
a = arange(10).reshape(2,5)
print "\nReshaped array = \n", a
print "\nArray shape = \n", a.shape
