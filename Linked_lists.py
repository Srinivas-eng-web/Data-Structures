""" linked_list : A linked list is a linear data structures where the elements (nodes) are stored in non-continuous  memory location ,Each node contains
1.Data (The value stored)
2.A refernce (pointer ) to the next node or address of the next node

Types :
1. Single linked list : Each node points to the next node
2.Doubly  linked list : Each nod points bothe next and previous node
3.Circular linked list : last node contains back to the first node
"""

# Basic Structure of a single linked list

class Node:
    def __init__(self,data):
        self.data = data  # value stored in node
        self.next = None  # Reference to the next node

#creating Basic linked_list structure

class Linked_list:
    def __init__(self):
        self.head = None # points to first node
#you have start some where ,so we give the address of the firstnode a special name called "head" also last node in the linked list can indentified because it next postion poins to Null


    def is_empty(self):
        return self.head is None


    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_after(self,prev_value,data): #start traversing from the head node.
        current = self.head # #current is a pointer used to move through the list.
        while current and current.data != prev_value: #This loop keeps moving to the next node until it finds the node with prev_value.

            current = current.next #If that value doesn’t exist, it eventually becomes None (end of the list).

            if not current:
                print(f"{prev_value} not found in the list")
                return

        new_node = Node(data) #Create a new node that will be inserted after the node with prev_value.
        new_node.next = current.next #new node’s .next should point to whatever the current node was pointing to. keeps the link with the rest of the list.
        current.next = new_node #Now we update the current node’s .next to point to our new node.inserts the new node right after the matched node.

    def delete(self,value):
        current = self.head
        # Case 1: List is empty
        if not self.head:
            print("list is empty")  #Just prints a message. Nothing to delete.
            return
            # Case 2: Node to delete is the head  ,Node is head	We reassign head to point to the second node.
        if current and current.data == value:
            self.head = current.next
            current = None
            return
            # Case 3: Node is somewhere else in the list ,
        #Node is in the middle/end	Traverse to find it, then update the next pointer of the previous node.
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if not current:
            print(f"{value}not found in the list")
            return
        prev.next = current.next
        current = None


    #display the list:
    def display(self):
        if self.is_empty():
            print("linked is empty")
            return
        current  = self.head

        while current:
            print(current.data , end="-->>")
            current = current.next
        print("None")

# Create linked list and insert elements
if __name__ ==  "__main__":
    l1 = Linked_list()
    l1.insert_at_end(10)

    l1.insert_at_end(20)
    l1.insert_at_end(30)
    l1.insert_after(30,40)
    l1.display() #output : 10-->>20-->>30-->>40-->>None

    l1.delete(20)
    l1.display()   #output : 10-->>30-->>40-->>50-->>None

    l1.delete(10)
    l1.display()  #output
    # 30-->>40-->>50-->>None
