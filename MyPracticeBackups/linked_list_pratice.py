
class Node:
    def __init__(self,data):
        self.head = head
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

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

    # def insert_at_begining(self,data):
    #     new_node = Node(data) # Step 1: Create a new node with given data
    #     new_node.next = self.head # Step 2: Link new node to current head (could be None)
    #     self.head = new_node  # Step 3: Update head to new node

    # def print_list(self):
    #     cur = self.head
    #     while cur:
    #         print(cur.data , end="->")
    #         cur = cur.next
    #     print("None")
    def print_list(self):
        current = self.head
        while current:
            print(current.data,end="-->")
            current = current.next
        print("None")

# if __name__ == "__main__":
#     l1 = LinkedList()
#     l1.insert_at_begining(12)
#     l1.insert_at_begining(20)
#     l1.print_list()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Linked_List:
#     def __init__(self):
#         self.head = None
#
#
#     def insert_at_end(self,data):
#         new_node = Node(data)
#
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#
#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data , end="->")
#             current = current.next
#         print("None")
# if __name__ == "__main__":
#     l1 = Linked_List()
#     l1.insert_at_end(12)
#     l1.insert_at_end(23)
#     l1.insert_at_end(30)
#     l1.print_list()


# class Node:
#     def __init__(self,data):
#         self.data  = data
#         self.next = None
#
# class Linked_List:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_begining(self,data):
#         new_node = Node(data)
#         new_node.next = new_node
#         self.head = new_node
#
#     def insert_at_end(self,data):
#         new_node = Node(data)
#
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#
#         while current.next:
#             current = current.next
#
#         current.next = new_node
#
#
#     def print_list(self):
#         current = self.head
#
#         while current:
#             print(current.data ,end= ">>")
#             current = current.next
#         print("None")
#
# if __name__ == "__main__":
#     l1 = Linked_List()
#     l1.insert_at_begining(10)
#     l1.insert_at_begining(20)
#
#     l1.insert_at_end(30)
#     l1.print_list()
#
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class Linked_List:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_end(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#
#         while current.next:
#             current = current.next
#
#         current.next = new_node
#
#     def insert_at_begining(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

    # Delete a node by value
    # def delete_node(self,key):
    #     current = self.head
    #
    #     if current and current.data == key:
    #         self.head = current.next
    #         current  = None
    #         return

    def 
        # # Case 2: Traverse to find the key
        # prev = None
        # while current and current != key:
        #     prev = current
        #     current = current.next
        #
        # if current is None:
        #     print(f"node with value {key} not found")
        #
        # prev.next = current.next
        # current = None

#     def delete_node(self,key):
#         current = self.head
#         if current and current.data == key:
#             self.head = current.next
#             current = None
#             return
#         #case 2 traverse to find the key
#         prev = None
#         while current and current.data != key:
#             prev = current
#             current = current.next
#         prev.next = current.next
#
#         if current is None:
#             return
#         prev.next = current.next
#         current = None
#
#
#
#
#     def print_list(self):
#         cur = self.head
#         while cur:
#             print(cur.data ,end="-->")
#             cur = cur.next
#         print("None")
# ll = Linked_List()
# ll.insert_at_end(10)
# ll.insert_at_end(20)
# ll.insert_at_end(30)
# ll.insert_at_end(40)
#
# print("Original List:")
# ll.print_list()
#
# # Delete a middle node
# ll.delete_node(30)
# print("\nAfter deleting 30:")
# ll.print_list()
#
# # Delete the head
# ll.delete_node(10)
# print("\nAfter deleting 10 (head):")
# ll.print_list()
#
# # Delete a non-existent node
# ll.delete_node(100)
#
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class Linked_List:
#     def __init__(self):
#
#         self.head = None
#
#
#     def insert_at_end(self,data):
#         new_node = Node(data)
#         current = self.head
#         if not self.head:
#             self.head = new_node
#             return
#         while current.next:
#             current = current.next
#
#         current.next = new_node
#
#     def delete_node(self,data):
#
#         # 1: Check if list is empty
#         if not self.head:
#             return "list is empty"
#
#
#         if self.head.data == key:
#             self.head  = self.head.next
#             return
#         # Step 3: Search for the node to delete in the rest of the list
#         current  = self.head
#         while current.next and current.next != key:
#

    #
        # if not self.head:
        #     return "empty"
        #
        # current = self.head
        # if current and current.data == data:
        #     self.head  = current.next
        #     current = None
        #     return
        # prev =  None
        #
        # while current and current != data:
        #     prev = current
        #     current = current.next
        # if not current:
        #     print(f"{data} is not in list")
        #     return
        #
        # prev.next = current.next
        # current = None

#
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data ,end="-->")
#             current = current.next
#         print("None")
#
# if __name__ == "__main__":
#     l1 = Linked_List()
#     l1.insert_at_end(10)
#     l1.insert_at_end(20)
#     l1.insert_at_end(30)
#     l1.display()
#     l1.delete_node(20)
#     l1.display()




class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node  = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node


    def delete_node(self,data):

        current = self.head


        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if not current:
            print(f"{data} is not in list")
            return

        prev.next = current.next
        current = None

    def insert_at_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("none")



if __name__ == "__main__":
    l1 = Linked_list()
    l1.insert_at_end(1)
    l1.insert_at_end(2)
    l1.insert_at_end(3)
    l1.insert_at_end(4)
    l1.insert_at_end(5)

    l1.display()
    l1.delete_node(3)

    l1.display()
    l1.insert_at_begin(6)
    l1.display()



