# ------------ Depth First Traversal ------------
# these general DFT are not pre-order
# the 'pre' order has to recursively maintained through the
# graph, but we can't ensure that because the each node's neighbors's order can't be predetermined.

# Run-time: O(V+E)
# Space: O(V)
	
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
	return visited
