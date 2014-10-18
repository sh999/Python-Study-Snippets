'''
String manipulations.py

Create a string and a substring
Print the ith character in the string length of string
Print the length of string
Print the index of character in string 
Print string with capitalization form
Print the string at a specific position 
	Do same but instead fill in spaces with '*'
Print how many times a substring appears in the string




'''
s = "hello world world!"
substring = "world"
print "Original string =",s
print "The 3rd character in \"",s,"\"is",s[2]
print "Length of string = ",len(s)
print "The letter o appears",s.count('o'),"many times"
print "The first letter o is in the position",s.find('o')
print "Capitalized =",s.capitalize()
print s.center(29,"*")
print substring,"occurs",s.count(substring),"many times in",s

