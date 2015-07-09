'''
readwrite
A study on reading/writing files

Tasks:
Create a file object and print it (not its content) and describe the output
What does readline() do?
Print all lines from the file
What does readlines() do? 
Create a file object that has both read and write modes
Write a line into the file
'''

f = open("sampletext.txt")
print f 	#	It shows the file name, mode (read or write) and memory address
# print f.readline()	#	Print one line at a time, and the file object remembers which line has been read
# print f.readline()
for line in f:	#	Prints all lines
	print line
g = open("sampletext.txt")
print g.readlines()	#	Presents all lines in file as list of strings
h = open("sampletext.txt", 'r+')	#	r+ ensures read+write
h.write("New line written")
print h.readlines()