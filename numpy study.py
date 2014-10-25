'''
numpy study.py

Tasks:
======
Use numpy to create arrays
	Create a "raw" array object where you give it actual values
	Create an automatic array where numpy creates an arrange based on given range
Reshape the arrays, and describe the shapes

References:
===========
http://wiki.scipy.org/Tentative_NumPy_Tutorial
'''
from numpy import *
a1 = array([1,2,3,4,5,6])
print "Raw array = ", a1
a1 = a1.reshape(2,3)
print "Reshaped array = ", a1
print "Array shape = ", a1.shape
a2 = arange(10)
print "Automatic array =", a2
a2 = a2.reshape(5,2)
print "Reshaped array =",a2
print "Array shape = ", a2.shape

