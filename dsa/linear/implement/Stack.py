# LIFO (Last In, First out)
# a list can be used with no loss in performance
# can be imported from collections import deque
#     lifo = deque()
#     lifo.append(l)
#     lifo.pop()

class Stack():
    def __init__(self):
        self.__stack = []

    def isEmpty(self):
        return len(self.__stack) == 0

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.__stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.__stack[-1]

    def getAll(self):
        return self.__stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(24)
print("----Regular Stack----" )
print(s.peek())
print(s.getAll())
print("\n")


"""
**Properties**:
- Last In.First Out [LIFO] -  the last element you add, is the first you'll remove 
    - mental model - [VERTICAL STACK OF BOOKS ON A TABLE]
- implemented with an array or linked list

**Basic Operations**
- push
- pop
- isEmpty
- isFull (only when implemented with a static array)
- peek

**Efficiency Rating**
|   Strengths        |       Weakness      |
|      :---:         |        :---:        |
| Retrieving | ` O(n) ` |          -          |
| -                  |  Inserting | "Push" ` O(1) ` |
| -                  |  Deleting  | "Pop" ` O(1) `  |
| -                  |  Searching ` O(n) ` |

"""