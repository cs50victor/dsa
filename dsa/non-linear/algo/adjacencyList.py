edgeList = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]

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