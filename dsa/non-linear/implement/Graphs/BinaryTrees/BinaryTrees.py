""" Binary trees are n-ary (n=2), out-trees with at most two child nodes 

IMPLEMENTING BINARY TREES
-------------------------
1. Using dynamically created Node objects
2. Using arrays
	- root =  arr[0]
	- for a node at index i (complete binary tree)
		- leftChild = 2i+1
		- rightChild = 2i+2
		- parentNode = int((i-1)/2)

TYPES OF BINARY TREES
---------------------
1. Complete Binary Tree: 
	- every level has nodes and far left as possible (except possibly the leaf nodes)
2. Perfect Binary Tree:
	- all internal nodes have 2 children and all outer nodes are on the same level
3. Strict/Full Binary Tree:
	- all nodes have at either 2 or 0 child nodes
3. Balanced Binary Tree:
	- the difference between the height of the left and right subtree for every node is not more than 1.
	- difference = |abs(height of left tree) - abs(height of right tree)|

SOME USEFUL FACTS FOR ALL BINARY TREES
--------------------------------------

1. # of leaf nodes = # of nodes with 2 children + 1
2. maximum # of nodes at a level  = 2 ^ (L-1)
3. maximum # of nodes in a tree of height h  = 2^(H+1) -1

Binary Heaps and Binary Search Trees common implementions of a binary tree
"""

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

root = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(-1)
		
root.left  = b
root.right = c
b.left  = d
b.right = e
c.right = f

# ------  SAME TRAVERSALS AS OTHER TREES -------

def preOrder(root):
	if root == None:
		return []
	# implicit call stack used in recursion
	return [root.value] + preOrder(root.left) + preOrder(root.right)
	
def inOrder(root):
	if root == None:
		return []
	# implicit call stack used in recursion
	return inOrder(root.left) + [root.value] + inOrder(root.right)
	
def postOrder(root):
	if root == None:
		return []
	# implicit call stack used in recursion
	return postOrder(root.left) + postOrder(root.right) + [root.value]
	
def levelOrder(root):
	if root == None:
		return []

	queue = [root]
	results = []
	while len(queue)>0:
		currNode = queue.pop(0)
		results.append(currNode.value)

		if currNode.left != None:
			queue.append(currNode.left)
		if currNode.right != None:
			queue.append(currNode.right)
	return results


print("PRE-ORDER")
print(preOrder(root))
print("IN-ORDER")
print(inOrder(root))
print("POST-ORDER")
print(postOrder(root))
print("LEVEL-ORDER")
print(levelOrder(root))

