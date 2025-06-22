"""What is a Tree?
A tree is a hierarchical data structure that mimics a tree in nature - it has a root, branches, and leaves. Unlike arrays
or linked lists that are linear, trees organize data in parent-child relationships.

Hierarchical = organized in levels or ranks, like a pyramid or ladder, where things are arranged from top to bottom with clear relationships.
Key Characteristics:
One root node at the top
Each node can have multiple children
No cycles (can't loop back)
Every node (except root) has exactly one parent

Types of Trees & Their Uses
Binary Trees
What: Each node has at most 2 children
Used for: General hierarchical data, expression parsing
Binary Search Trees (BST)
What: Left child < parent < right child
Used for: Fast searching, sorting, maintaining ordered data
Example: Auto-complete suggestions, phone contacts
Heaps
What: Parent is always larger (max-heap) or smaller (min-heap) than children
Used for: Priority queues, task scheduling, finding top K elements
Example: Operating system task scheduling
Tries
What: Tree where each path represents a word/string
Used for: Autocomplete, spell checkers, IP routing
Example: Google search suggestions
"""
# Tree structure
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#Tree Traversals
#Preorder (Root ➜ Left ➜ Right)
#Inorder (Left ➜ Root ➜ Right)
#Postorder (Left ➜ Right ➜ Root)
def preorder(root):
    if root:

        print(root.val , end="-->")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val ,end="-->")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val ,end="-->")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.left.left.left = TreeNode(6)

preorder(root) #output 1-->2-->4-->6-->3-->5-->

inorder(root)  #output : 6-->4-->2-->1-->5-->3-->

postorder(root) #6-->4-->2-->5-->3-->1-->


