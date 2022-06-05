"""
Binary Search Tree — ia binary tree with the constraint:
- left subtree < currNode < right subtree

The left and right subtree each must also be a binary search tree.

"""

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class BST:
	def __init__(self):
		self.root = None

	def add(self, value):
		if self.root == None:
			self.root = Node(value)
		else:
			stack = [self.root]
			while len(stack)>0:
				currNode = stack.pop()

				if value < currNode.value:
					if currNode.left == None:
						currNode.left = Node(value)
					else:
						stack.append(currNode.left)
				elif value > currNode.value:	
					if currNode.right == None:
						currNode.right = Node(value)
					else:
						stack.append(currNode.right)
	
	def contains(self, value):
		if self.root == None:
			return False

		stack = [self.root]
		
		while len(stack)>0:
			currNode = stack.pop()

			if currNode.value == value:
				return True

			if value < currNode.value:
				if currNode.left == None:
					return False
				stack.append(currNode.left)
			elif value > currNode.value:
				if currNode.right == None:
					return False
				stack.append(currNode.right)
		
		return False

	def findMin(self):
		if self.root == None:
			return float("-inf")

		stack = [self.root]

		while len(stack)>0:
			currNode = stack.pop()

			if currNode.left == None:
				return currNode.value
			stack.append(currNode.left)

	def findMax(self):
		if self.root == None:
			return float("inf")

		stack = [self.root]

		while len(stack)>0:
			currNode = stack.pop()

			if currNode.right == None:
				return currNode.value
			stack.append(currNode.right)

	def preOrderTraversal(self):
		if self.root == None:
			return 
		
		allNodes = []
		stack = [self.root]

		while len(stack)>0:
			currNode = stack.pop()

			allNodes.append(currNode)
			if currNode.right != None:
				stack.append(currNode.right)
			if currNode.left != None:
				stack.append(currNode.left)
	
	def printTree(self):
		# pre order traversal (DFS)
		if self.root == None:
			return 
		#      (node, level)
		stack = [(self.root, 0)]
	
		while len(stack)>0:
			currNode, level = stack.pop()
			line = "\t|_" * level + f"({currNode.value})"+"\n"
			print(line, end="")
			if currNode.right != None:
				stack.append((currNode.right, level+1))
			if currNode.left != None:
				stack.append((currNode.left, level+1))

bst = BST()
for value in [17,4,1,20,9,23,18,34]:
	bst.add(value)

bst.printTree()

bst2 = BST()
nums = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48, 1, 8, 15, 45, 50]
for value in nums:
	bst2.add(value)

bst2.printTree()