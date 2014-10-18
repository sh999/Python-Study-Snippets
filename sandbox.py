'''
sandbox.py
'''
# Read a file
f = open("sampetext.txt") # Open a file lines = (t.strip() for t in f) # Read lines, strip
# trailing/leading whitespace comments = (t for t in lines if t[0] == ‘#’) # All comments
for c in comments: print c