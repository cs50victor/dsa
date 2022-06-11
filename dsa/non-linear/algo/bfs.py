from collection import deque
# ------------  Breadth First Traversal ------------
# BFT can only be done iterative using a queue because recursions use an implicit call stacks
# Run-time: O(V+E)
# Space: O(V)

# used in path finding algorithms, GPS navigation, minimum spannig tree, cycle detection in an undirected graph


def bftNoSet(graph, node):
	# directed acyclic graph 
    queue = deque([node])
    while queue:
        currNode = queue.popleft()
        print(currNode)
        for neighbor in graph[currNode]:
            queue.append(neighbor)

def bft(graph, node):
    visited = set()
    queue = deque([node])
    while queue:
        currNode = queue.popleft()
        visited.add(currNode)
        print(currNode)
        for neighbor in graph[currNode]:
            if neighbor not in visited:
                queue.append(neighbor)