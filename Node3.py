class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data, end=" ")
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
postorderTraversal(root)