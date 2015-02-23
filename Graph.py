'''
Implementation of graph data structure
References
==========
https://www.python.org/doc/essays/graphs/
'''
#Implement graph with dictionary; key is node, and value is a list of subsequent nodes emanating from key node
def find_path(graph, start, end, path=[]): #Default value for path only assigned if argument wasn't passed with a value
	path = path + [start]
	if start == end:
		return path
	if not graph.has_key(start):
		print 'Starting key not found'
		return None
	for node in graph[start]: #Iterates through value of key graph[start]
		print 'Node = ', node
		if node not in path:
			print 'Node not in path'
			newpath = find_path(graph, node, end, path) #Recursion.  Backtrack occurs when a node is found that is already in path
			print 'New path = ', newpath
			if newpath: return newpath
	print 'Nothing found'
	return None

def main():
	graph = { 'A': ['B', 'C'],
	   	 	  'B': ['C', 'D'],
	   	 	  'C': ['A'],
	   	 	  'D': ['F'],
	   	 	  'E': ['F'],
	   	 	  'F': ['C']}
	print find_path(graph, 'A', 'F')

main()

'''mydict = { "key1": 1,
            "key2": 2,
           "key3": 3, }'''