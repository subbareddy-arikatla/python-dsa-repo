class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


# def search(root,key):
#     if root is None:
#         return False
#     if root.data == key:
#         return True
#     if root.data>key:
#         return search(root.left,key)
#     return search(root.right,key)

def search(root, key):
    while root is not None:
        if root.data == key:
            return True
        elif key < root.data:
            root = root.left
        else:
            root = root.right
    return False

root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.right.left = Node(7)
root.right.right = Node(9)
key = 9
print(search(root, key))

