'''
Tasks:
Create a string that holds a sentence 
Create a list that holds a character of strings from above
Create a list that holds words from the sentence
Create a string that has data separated by commas
Create a list form the data above but separate by commas
Rejoin the data but replace commas with dashes
'''

sentence = "Hello, world!  My name is Bob."
listOfChars = list(sentence)
listOfWords = sentence.split()
data = "Bob,20 years old,Male"
splitData = data.split(",")
joinedData = "-".join(splitData)
print "Sentence = ", sentence
print "List of characters = ", listOfChars
print "List of words = ", listOfWords
print "Data = ", data
print "Split data = ", splitData
print "Rejoined data = ", joinedData
