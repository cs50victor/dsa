# python's implementation uses a doubly-linked list
# insert or remove from both ends
# from collections import deque

class Deque:
    def __init__(self):
        self.__deque = []

    # Check if deque is empty
    def isEmpty(self):
        return len(self.__deque) == 0

    # Add an item to the front of the deque
    def append(self, item):
        self.__deque.append(item)

    # Add an item to the back of the deque
    def appendLeft(self, item):
        self.__deque.insert(0,item)

    # Remove an item from the front of the deque
    def pop(self):
        if not self.isEmpty():
            return self.__deque.pop()

    # Remove an item from the back of the deque
    def popLeft(self):
        if not self.isEmpty():
            return self.__deque.pop(0)
            
    # Get the item at the front of the deque
    def peek(self):
        if not self.isEmpty():
            return self.__deque[-1]
            
    # Get the item at the back of the deque
    def peekLeft(self):
        if not self.isEmpty():
            return self.__deque[0]

    # Get all elements in the Queue
    def getAll(self):
        return self.__deque