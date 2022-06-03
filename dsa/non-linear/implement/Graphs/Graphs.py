"""
****ALL NON-LINEAR DATA TYPES ARE GRAPHS*******

A graph is an Abstract Data Type (ADT) that can be used to represent complex, non-linear relationships between objects. A graph consists of nodes (also called vertices) that are connected by edges (also called arcs).


- Graph-traversal is the process of visiting each vertex in a graph. 

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

Graphs:
    1. Directed Graphs (Digraph)  '->' one-way direction
    2. Undirected Graphs          '-'  two-way direction
		- utilizes a set to avoid an infinite loop

Key words:
    - Node
    - Neighbour Nodes (Nodes accessible by a node)
	- adjacency list ( a dictionary 
									key :  value
									Node: [neighbor nodes]
					 )
	- edges (connection between two nodes)
"""

# ADJACENCY LIST REPRESENTATION
# -- directed graph --
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
# -- iterative


def dft(graph, node):
    stack = [node]
    while len(stack) > 0:
        currNode = stack.pop()
        print(currNode)
        for neighbor in graph[currNode]:
            stack.append(neighbor)


# -- recursive (recursion stack or "the call stack " )
def dftRecursive(graph, node):
    print(node)
    neighbors = graph[node]
    for neighbor in neighbors:
        dftRecursive(graph, neighbor)


# ------------  Breadth First Traversal ------------
# only iterative implementation as recursions use an implicit stacks


def bft(graph, node):
    queue = [node]
    while len(queue) > 0:
        currNode = queue.pop(0)
        print(currNode)
        for neighbor in graph[currNode]:
            queue.append(neighbor)


# Big O analysis

# n = # of nodes
# e (or n^2) = # of edges

# space = O(n)
# time = o(e)


# --- acyclic directed graph
def hasPathDFS(graph, src, dst) -> bool:

    if (src == dst):
        return True

    for neighbor in graph[src]:
        if hasPathDFS(graph, neighbor, dst) == True:
            return True

    return False


def undirectedPath(graph, nodeA, nodeB):
    return hasPathDFSUndirected(graph, nodeA, nodeB, set())


def hasPathDFSUndirected(graph, src, dst, visited) -> bool:
    if (src == dst): return True
    if (src in visited): return False

    visited.add(src)
    for neighbor in graph[src]:
        if hasPathDFSUndirected(graph, neighbor, dst, visited) == True:
            return True
    return False


def hasPathBFS(graph, src, dst) -> bool:

    queue = [src]

    while len(queue) > 0:
        currNode = queue.pop(0)
        if currNode == dst:
            return True
        for neighbor in graph[currNode]:
            queue.append(neighbor)

    return False


def converToAdjacencyLsit(edgeList):

    adjacencyList = {}
    for edge in edgeList:
        nodeA, nodeB = edge
        if nodeA not in adjacencyList:
            adjacencyList[nodeA] = []
        if nodeB not in adjacencyList:
            adjacencyList[nodeB] = []
        adjacencyList[nodeA].append(nodeB)
        adjacencyList[nodeB].append(nodeA)
