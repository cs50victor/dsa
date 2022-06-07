"""
Binary Heaps are complete binary tree (filled on every level from left to right)

Types:
1. Min-Heap (recursively - the parent node is the max in the tree - child nodes are also trees)
2. Max-Heap (recursively - the parent node is the min in the tree - child nodes are also trees)
sometimes implemented with an array under the hood

leftChild = 2i+1
rightChild = 2i+2
parent = (i-1)/2
import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)

print(H)

Insertion O(log n)
O(logn)
: Finding the exact position of the new element is performed in log n
logn
 since it is only compared with the position of the parent nodes.
Delete Min O(log n)
O(logn)
: After the minimum element is removed, the heap has to put the new root in place.
Find Min O(1)
O(1)
: This is possible because the heap data structure always has the minimum element on the root node.
Heapify O(n)
O(n)
: This operation rearranges all the nodes after deletion or insertion operation. The cost of this operation is n
n
 since all the elements have to be moved to keep the heap properties.
Delete O(log n)
O(logn)
: A specific element from the heap can be removed in log n
logn
 time.

"""
from random import randint 

class MinHeap:
	def __init__(self):
		self.__heap = []

	def __getParentindex__(self, index):
		return (index-1)//2

	def __getRightChildIndex__(self, index):
		return 2 * index +2

	def __getLeftChildIndex__(self, index):
		return 2 * index + 1
		
	def __hasParent__(self, index):
		return self.__getParentindex__(index) >= 0

	def __hasRightChild__(self, index):
		return self.__getRightChildIndex__(index) < len(self.__heap)

	def __hasLeftChild__(self, index):
		return self.__getLeftChildIndex__(index) < len(self.__heap)

	def __parent__(self, index):
		return self.__heap[self.__getParentindex__(index)]

	def __rightChild__(self, index):
		return self.__heap[self.__getRightChildIndex__(index)]

	def __leftChild__(self, index):
		return self.__heap[self.__getLeftChildIndex__(index)]
		
	def __swap__(self, indexA, indexB):
		self.__heap[indexB],self.__heap[indexA] = self.__heap[indexA], self.__heap[indexB] 
		
	def peek(self):
		if len(self.__heap)==0:
			return
		return self.__heap[0]
	
	def heappop(self):
		if len(self.__heap)==0:
			return
		minValue = self.__heap[0]
		self.__heap[0] = self.__heap[-1]
		self.__heap.pop()
		self.__heapifyDown__()
		return minValue

	def heappush(self, value):
		self.__heap.append(value)
		self.__heapifyUp__()
	
	def __heapifyUp__(self):
		index = len(self.__heap)-1
		"""
		while the last number in the heap has a parent and that parent is 
		greater than it, keep swapping
		"""
		while(self.__hasParent__(index) and self.__parent__(index) > self.__heap[index]):
			self.__swap__(index, self.__getParentindex__(index))
			index = self.__getParentindex__(index)
		
	def __heapifyDown__(self):
		index = 0
		while self.__hasLeftChild__(index):
			smallerChildIndex = self.__getLeftChildIndex__(index)
			if self.__hasRightChild__(index) and self.__rightChild__(index) < self.__leftChild__(index):
				smallerChildIndex = self.__getRightChildIndex__(index)

			if self.__heap[index] < self.__heap[smallerChildIndex]:
				break
			self.__swap__(index, smallerChildIndex)
			index = smallerChildIndex
				
		
class MaxHeap(MinHeap):
	def __init__(self):
		super().__init__()

	def __heapifyUp__(self):
		index = len(self._MinHeap__heap)-1
		"""
		while the last number in the heap has a parent and that parent is 
		greater than it, keep swapping
		"""
		while(self.__hasParent__(index) and self.__parent__(index) < self._MinHeap__heap[index]):
			self.__swap__(index, self.__getParentindex__(index))
			index = self.__getParentindex__(index)
		
	def __heapifyDown__(self):
		index = 0
		while self.__hasLeftChild__(index):
			biggerChildIndex = self.__getLeftChildIndex__(index)
			if self.__hasRightChild__(index) and self.__rightChild__(index) > self.__leftChild__(index):
				biggerChildIndex = self.__getRightChildIndex__(index)

			if self._MinHeap__heap[index] > self._MinHeap__heap[biggerChildIndex]:
				break
			self.__swap__(index, biggerChildIndex)
			index = biggerChildIndex
	

heap1 = MinHeap()
heap2 = MaxHeap()

y = []
z = 70
for i in range(z):
	x = randint(0,i)
	y.append(x)
	heap1.heappush(x)
	heap2.heappush(x)


y = sorted(y)
x = y[::-1]
for i in range(z):
	print(f"MIN {y[i]}=={heap1.heappop()}, MAX {x[i]}=={heap2.heappop()}")