"""
Space: O(N^2)
Useful when there are a lot of edges between nodes
- or for GPU matrix operations

[nodeA][nodeB] = weight or (1 for edge, 0 for no edge)

"""
width, height = 10,10 

def createMatrix(x, y):
	adjMatrix = []
	for i in range(y):
		adjMatrix.append([0 for _ in range(x)])
	return adjMatrix

# Add edges O(1)
def addEdge(adjMatrix, v1, v2):
	if v1 > width or v2 > height:
		print("invalid vertex index")
		return 
	adjMatrix[v1][v2] = 1
	adjMatrix[v2][v1] = 1

# Remove edges O(1)
def removeEdge(adjMatrix, v1, v2):
	if v1 > width or v2 > height:
		print("invalid vertex index")
		return 
	elif adjMatrix[v1][v2] == 0:
		print("No edge between %d and %d" % (v1, v2))
		return
	adjMatrix[v1][v2] = 0
	adjMatrix[v2][v1] = 0

def printMatrix(adjMatrix):
	for row in adjMatrix:
		print(row)

graph = createMatrix(width, height)

