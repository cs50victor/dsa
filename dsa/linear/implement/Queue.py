# FIFO (First In, First Out)
# using a list makes dequeue an O(n) operation
# can be imported - from collections import deque
# implementation
#     fifo=deque()
#     fifo.append(l)
#     fifo.popleft()

class Queue:
    def __init__(self):
        self.__queue = []

    # Check if queue is empty
    def isEmpty(self):
        return len(self.__queue) == 0

    # Add an element
    def enqueue(self, element):
        self.__queue.append(element)

    # Remove an element
    def dequeue(self):
        if not self.isEmpty():
            return self.__queue.pop(0)

    # Get the element at the front of the queue
    def peek(self):
        if not self.isEmpty():
            return self.__queue[0]

    # Get all elements in the Queue
    def getAll(self):
        return self.__queue


"""
**Properties**:
- Like an opposite of the stack
- First In.First Out [FIFO] -  the first element you add, is the first you'll remove 
    - mental model - [ PEOPLE WAITING ON A QUEUE AT CINEMA, FIRST PERSON THERE IS THE FIRST TO GET A TICKET]
- implemented with a dynamic array or a doubly linked list

**Basic Operations**
- enqueue / adding to the queue => O(1) | O(n) if using dynamic array
- dequeue / remove an element out of the queue => O(1) | O(n) if using dynamic array
- peek at the element at the front of the queue => O(1)
- searching => O(n)
- isEmpty
- isFull (only when implemented with a static array)

**Efficiency Rating**
|   Strengths        |       Weakness      |
|      :---:         |        :---:        |
| Retrieving | ` O(n) ` |          -          |
| -                  |  Inserting | "Push" ` O(1) ` |
| -                  |  Deleting  | "Pop" ` O(1) `  |
| -                  |  Searching ` O(n) ` |

"""