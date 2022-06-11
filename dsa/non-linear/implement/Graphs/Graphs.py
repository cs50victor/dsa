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

Spanning Tree:
--------------
A spanning tree is a sub-graph of an undirected connected graph, which includes all the nodes of the graph with a minimum possible number of edges. 
* # of spanning trees that can created from a complete graph = n^(n-2)
- where n is the number of nodes
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


# Big O analysis
# n = # of nodes
# e (or n^2) = # of edges
# time = o(e)
# space = O(n)