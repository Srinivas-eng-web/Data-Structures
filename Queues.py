"""what is Queue : Queue is Frist in First out
Think : a line at ticket counter - the first person to enter served first
Read word examples:
1.printers task Queues
2.Custmer service lines
3.order proccessing
4.Message queue in distubtion system
Basic operations :
enqueue : Add to the end of the stack
dequeue : remove from the front the stack
peek : see front one without removing
is_empty: check if the queue is empty
"""


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add to end

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self, item):
        if self.is_empty():
            return None

        return self.items.pop(0)  # remove from the first

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(f"size of Queue,{q.size()}")
print(f"Dequeue element is {q.dequeue(20)}")
print(f"the peek element is {q.peek()}")
print(f"isempty {q.is_empty()}")


# Queue using Stack problem:
class QueueusingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

            return self.stack_out.pop()

    def peek(self):
        if self.isempty():
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

            return self.stack_out[-1]

    def is_empty(self):
        return not self.stack_in and self.stack_out


Q = QueueusingStacks()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
print(Q.dequeue())
print(Q.is_empty())  #

"""Circular Queue : A circular Queue is a fixed-size Queue where the last option wraps
aroundto the first position.
-> instead of shifting all element when dequeueing (like in regular list) , we use module(%)
to wrap around -making it space efficent
we maintain :
queue : fixed-size list
front : index of front element
rear : index where to insert next
size : no,of current elements 
we wrap around using 
index = (index+1)%capacity

"""


class CircularQueue:
    def __init__(self, k):
        self.size = 0
        self.rear = 0
        self.Queue = [None] * k
        self.capacity = k
        self.front = 0

    def isempty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.isFull():
            return False

        self.Queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.isempty():
            return False
        self.Queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def get_front(self):
        if self.isempty():
            return -1
        return self.Queue[self.front]

    def get_rear(self):
        if self.isempty():
            return -1
        return self.Queue[(self.rear - 1 + self.capacity) % self.capacity)]





        # "Implement Stack or Queue using Array or Linked List."

        # 1.. Stack using Array (Python list)

        class StackArray:
            def __init__(self):
                self.stack = []

            def push(self, item):
                self.stack.append(item)
                return self.stack

            def pop(self):
                if not self.is_empty():
                    return self.stack.pop()

            def peek(self):
                if not self.is_empty():
                    return self.stack[-1]
                return None

            def is_empty(self):
                return len(self.stack) == 0

        a = StackArray()
        print(a.push(29))
        print(a.push(2))

        # Stack using Linked List

        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None

        class Linkedlist:
            def __init__(self):
                self.top = None

            def push(self, item):
                new_node = Node(data)
                new_node.next = self.top
                self.top = new_node

            def pop(self):
                if self.is_empty():
                    return None
                popped = self.top.value
                self.top = self.top.next
                return popped

            def is_empty(self):
                return self.top is None
