class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data, end = " ")
        inorderTraversal(root.right)
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(6)
root.right.right.left = Node(10)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.left.right.rignt = Node(9)
inorderTraversal(root)
