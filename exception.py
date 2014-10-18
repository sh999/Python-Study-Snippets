'''
exception.py

Simple case:
Try opening a file, feed it a file that can't be opened/doesn't exist
Raise exception and display your own error message
'''
try:
	open("samdpletext.txt").readlines()
except IOError:
	print "File not found"