from collections import deque
"""
A n-ary tree is an ordered rooted tree in which each node has at most n children. 2-ary trees are often called binary trees, while 3-ary trees are sometimes called ternary trees.

usually out-trees

ordered tree is an oriented tree in which children of a node are somehow 'ordered'
i.e we know node.left comes before node.right

  A          A
B   C   != C   B
"""

class TernaryTreeNode:
	def __init__(self, value, left=None,middle=None, right=None):
		self.value = value
		self.left = left
		self.middle  = middle 
		self.right = right

root = TernaryTreeNode("Electronics")

laptop = TernaryTreeNode("Laptop", TernaryTreeNode("Mac"),TernaryTreeNode("Surface"), TernaryTreeNode("Thinkpad"))

cellphone = TernaryTreeNode("Cell Phone")
cellphone.left = TernaryTreeNode("iPhone")
cellphone.middle = TernaryTreeNode("Google Pixel")
cellphone.right = TernaryTreeNode("Vivo")

tv = TernaryTreeNode("TV")
tv.left = TernaryTreeNode("Samsung")
tv.middle = TernaryTreeNode("LG")

root.left = laptop
root.middle = cellphone
root.right = tv

def preorderIterative(root):
	# pre order traversal (DFS)
	if root == None:
		return 
		
	stack = deque([root])
	allValues = []
	
	while stack:
		currNode = stack.pop()
		allValues.append(currNode.value)

		if currNode.right:
			stack.append(currNode.right)
		if currNode.middle:
			stack.append(currNode.middle)	
		if currNode.left:
			stack.append(currNode.left)
			
	return allValues


def inorderIterative(root):
	# in order traversal (DFS)
	if root == None:
		return 
		
	stack = deque()
	allValues = []
	currNode = root
	
	while stack or currNode:
		if currNode:
			stack.append(currNode)
			currNode = currNode.left
		else:
			currNode = stack.pop()
			allValues.append(currNode.value)
			currNode = currNode.middle
			# currNode = currNode.right
	return allValues

def postorderIterative(root):
	# post order traversal (DFS)
	if root == None:
		return 
	stack = deque([ root ])
	allValues = deque()
	
	while stack:
		currNode = stack.pop()
		allValues.appendleft(currNode.value)

		if currNode.right:
			stack.append(currNode.right)
		if currNode.middle:
			stack.append(currNode.middle)	
		if currNode.left:
			stack.append(currNode.left)
	return allValues

def preOrder(root):
	if root == None:
		return []
	# implicit call stack used in recursion
	return [root.value] + preOrder(root.left) +preOrder(root.middle)  + preOrder(root.right)
	
def inOrder(root):
	if root == None:
		return []
	# implicit call stack used in recursion
	return inOrder(root.left) + preOrder(root.middle) + [root.value] + inOrder(root.right)
	
def postOrder(root):
	if root == None:
		return []
	# implicit call stack used in recursion
	return postOrder(root.left) + preOrder(root.middle) + postOrder(root.right) + [root.value]
	
def levelOrder(root):
	if root == None:
		return []

	queue = deque([root])
	results = []
	while len(queue)>0:
		currNode = queue.popleft()
		results.append(currNode.value)

		if currNode.left != None:
			queue.append(currNode.left)
		if currNode.middle != None:
			queue.append(currNode.middle)
		if currNode.right != None:
			queue.append(currNode.right)
	return results




print("PRE-ORDER")
print("\t","->".join(preorderIterative(root)), "\n")
print("\t","->".join(preOrder(root)), "\n")
print("IN-ORDER")
# print("->".join(inorderIterative(root)))
print("\t","->".join(inOrder(root)), "\n")
print("POST-ORDER")
print("\t","->".join(postorderIterative(root)), "\n")
print("\t","->".join(postOrder(root)), "\n")
print("LEVEL-ORDER")
print("\t","->".join(levelOrder(root)),"\n")


p