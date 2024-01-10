class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left) # Traverse left subtree
        print(root.data, end=' ') # Visit node
        inorder_traversal(root.right) # Traverse right subtree

def preorder_traversal(root):
    if root:
        print(root.data, end=' ') # Visit node
        preorder_traversal(root.left) # Traverse left subtree
        preorder_traversal(root.right) # Traverse right subtree

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left) # Traverse left subtree
        postorder_traversal(root.right) # Traverse right subtree
        print(root.data, end=' ') # Visit node

# Creates a binary tree
root = TreeNode(1)  # Creates the root node with data 1.
root.left = TreeNode(2)  # Creates a left child of the root with data 2.
root.right = TreeNode(3)  # Creates a right child of the root with data 3.
root.left.left = TreeNode(4)  # Creates a left child of the node with data 2.
root.left.right = TreeNode(5)  # Creates a right child of the node with data 2.

# Outputting the tree structure
print("Inorder Traversal visits the left subtree, the node itself, and then the right subtree.:") 
inorder_traversal(root)
print("\nPreorder Traversal visits the node first, then the left subtree, followed by the right subtree.:")
preorder_traversal(root)
print("\nPostorder Traversal visits the left subtree, the right subtree, and then the node itself:")
postorder_traversal(root)