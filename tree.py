class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data,end=" ")
    inorder_traversal(root.right)
def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.right = Node(3)
root.left.left = Node(1)
root.right.left = Node(7)
root.right.right = Node(9)
root.left.right.left = Node(6)
print("inorder travalsal")
inorder_traversal(root)
print()
print("preorder travalsal")
preorder_traversal(root)
print()
print("postorder travalsal")
postorder_traversal(root)

