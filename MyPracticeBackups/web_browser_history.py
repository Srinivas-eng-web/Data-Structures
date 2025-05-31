#Step 1: Basic Setup — Node and LinkedList Classes
#Node class
class Node:
    def __init__(self,url):
        self.url = url
        self.next = None

# BrowserHistory class using Singly Linked List
class BrowserHistory:
    def __init__(self):
        self.head = None

#Step 2: Visit a New Page (Append to List)

    def visit_page(self,url):
        new_node = Node(url)
        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node


    def visit_page(self,url):
        new_node = Node(url)

        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node