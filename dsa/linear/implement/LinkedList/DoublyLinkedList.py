# can be imported from pip package llist
# i.e from llist import dllist, dllistnode
"""
In general, when there isn't a reference pointing to some object, this will be garbaged collected at some point.
! important when deleting elements
"""

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def __len__(self):
        return self.__size
        
    def __invalidIndex(self, index:int)->bool:
        return index<0 or index >= self.__size
        
    def get(self, index: int) -> int:
        # return -1 if index is invalid
        if self.__invalidIndex(index) or self.__head == None:
            return -1
            
        currNode = self.__head
        for _ in range(index):
            currNode = currNode.next
        return currNode.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.__size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if (index < 0 or index > self.__size):
            return 
        elif (index == 0):
            self.__head = Node(val,next=self.__head)
            if self.__head.next:
                self.__head.next.prev = self.__head
        else:
            currNode = self.__head
            for _ in range(index-1):
                currNode = currNode.next
            currNode.next = Node(val, currNode, currNode.next)
        self.__size +=1 

    def deleteAtHead(self) -> None:
        self.deleteAtIndex(0)
        
    def deleteAtTail(self) -> None:
        self.deleteAtIndex(self.__size-1)

    def deleteAtIndex(self, index: int) -> None:
        if self.__invalidIndex(index) or self.__head == None:
            return 
        elif (index == 0):
            self.__head = self.__head.next
            if(self.__head):
                self.__head.prev = None
        else:
            currNode = self.__head
            for _ in range(index-1):
                currNode = currNode.next
            if (currNode.next.next):
                currNode.next.next.prev = currNode
            currNode.next = currNode.next.next
        self.__size -= 1