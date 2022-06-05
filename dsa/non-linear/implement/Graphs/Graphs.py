"""
****ALL NON-LINEAR DATA TYPES ARE GRAPHS*******

A graph is an Abstract Data Type (ADT) that can be used to represent complex, non-linear relationships between objects. A graph consists of nodes (also called vertices) that are connected by edges (also called arcs).


1. Directed Graphs (Digraph)  '->' one-way direction
2. Undirected Graphs          '-'  two-way direction

WAYS OF REPRESENTING A GRAPH
1. ADJACENCY LIST
2. EDGE LIST
3. ADJACENCY MATRIX


Graph-traversal is the process of visiting each vertex in a graph. 
THERE ARE TWO MAIN METHODS OF TRAVERSING GRAPHS:
1. Depth First Traversal
    - uses a stack to keep track of nodes to visit
        - pops a node that is completely explored 
    - a branch/path/direction is fully explored before backtracking to other directions/paths/branches

2. Breadth-first Traversal 
    - uses a queue to keep track of nodes to explore
        - completely explored nodes are dequeued
        - node yet to be completely explored are enqueued
    - a node is fully explored before advancing to further nodes
	- all directions are explored evenly

Only times not to use a set during traversal
- directed acyclic graph 
- hierarchal tree

Key words:
    - Node
    - Neighbour Nodes (Nodes accessible by a node)
	- adjacency list ( a dictionary where a key is a node, and the value is list of all neighbor nodes )
	- edges (connection between two nodes)
	- complete graph (a graph where there is a unique edge between every pair of nodes- full cycles) 
"""

# ADJACENCY LIST REPRESENTATION
# -- directed acyclic graph --
graph = {"a": ["c", "b"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

# EDGE LIST REPRESENTATION
# -- undirected graph --
edgeList = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]

# ADJACENCY MATRIX REPRESENTATION
matrix = [[0, 1, 1, 0], [0, 0, 3, 0], [0, 0, 0, 4], [5, 0, 0, 0]]
# use 1 or weight to signify edge, else 0

def edgeToAdjacenyList(edgeList: list) -> dict:
    # reason: quick find for neighbor nodes
    adjList = dict()
    for edge in edgeList:
        nodeA, nodeB = edge
        if nodeA not in adjList:
            adjList[nodeA] = []
        if nodeB not in adjList:
            adjList[nodeB] = []
        adjList[nodeA].append(nodeB)
        adjList[nodeB].append(nodeA)
    return adjList


# ------------ Depth First Traversal ------------
# these general DFT are not pre-order
# the 'pre' order has to recursively maintained through the
# graph, but we can't ensure that because the each node's neighbors's order can't be predetermined.
	
# -- iterative
def dftNoSet(graph, node):
	# directed acyclic graph 
    stack = [node]
    while len(stack) > 0:
        currNode = stack.pop()
        print(currNode)
        for neighbor in graph[currNode]:
            stack.append(neighbor)

def dft(graph, node):
	visited = set()
    stack = [node]
    while stack:
        currNode = stack.pop()
		visited.add(currNode)
        print(currNode)
        for neighbor in graph[currNode]:
			if neighbor not in visited:
				stack.append(neighbor)
            	visited.add(neighbor)

# -- recursive (recursion stack or "the call stack " )
def dftRecursiveNoSet(graph, node):
	# directed acyclic graph 
    print(node)
    for neighbor in graph[node]:
        dftRecursiveNoSet(graph, neighbor)

def dftRecursive(graph, node, visited=set()):
    print(node)
	visited.add(node)
    for neighbor in graph[node]:
		if neighbor not in visited:
        	dftRecursive(graph, neighbor, visited)

# ------------  Breadth First Traversal ------------
# BFT can only be done iterative using a queue because recursions use an implicit call stacks

def bftNoSet(graph, node):
	# directed acyclic graph 
    queue = [node]
    while queue:
        currNode = queue.pop(0)
        print(currNode)
        for neighbor in graph[currNode]:
            queue.append(neighbor)

def bft(graph, node):
    visited = set()
    queue = [node]
    while queue:
        currNode = queue.pop(0)
        visited.add(currNode)
        print(currNode)
        for neighbor in graph[currNode]:
            if neighbor not in visited:
                queue.append(neighbor)

# Big O analysis
# n = # of nodes
# e (or n^2) = # of edges
# time = o(e)
# space = O(n)