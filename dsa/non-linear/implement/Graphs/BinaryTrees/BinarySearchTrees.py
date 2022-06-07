from collections import deque
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
		
		while stack:
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

	
	def preOrder(self):
		if self.root == None:
			return 
		
		allValues = []
		stack = [self.root]

		while stack:
			currNode = stack.pop()
			allValues.append(currNode.value)
			
			if currNode.left != None:
				stack.append(currNode.left)
			if currNode.right != None:
				stack.append(currNode.right)
		return allValues
		
	def inOrder(self):
		# in  order traversal (DFS)
		stack = []
		currNode = self.root
		allValues = []
		
		while stack or currNode:
			if currNode:
				stack.append(currNode)
				currNode = currNode.left
			else:
				currNode = stack.pop()
				allValues.append(currNode.value)
				currNode = currNode.right
		return allValues

		
	def postOrder(self):
		if self.root == None:
			return 
		
		allValues = deque()
		stack = [self.root]

		while len(stack)>0:
			currNode = stack.pop()
			allValues.appendleft(currNode.value)
			
			if currNode.right != None:
				stack.append(currNode.right)
			if currNode.left != None:
				stack.append(currNode.left)
		return list(allValues)
		
	def levelOrder(self):
		if self.root == None:
			return []
	
		queue = [self.root]
		results = []
		while len(queue)>0:
			currNode = queue.pop(0)
			results.append(currNode.value)
	
			if currNode.left != None:
				queue.append(currNode.left)
			if currNode.right != None:
				queue.append(currNode.right)
		return results

bst = BST()
nums = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48, 1, 8, 15, 45, 50]
for value in nums:
	bst.add(value)

print("\nPREORDER\n", bst.preOrder())
print("\nINORDER\n", bst.inOrder())
print("\nPOSTORDER\n", bst.postOrder())
print("\nLEVELORDER\n", bst.levelOrder())


