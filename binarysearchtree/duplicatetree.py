class Node:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(f"{root.key}({root.count})", end=" ")
        inorder(root.right)

def insert(root,key):
    if root is None:
        return Node(key)
    if key==node.key:
        node.count+=1
        return Node
    if key < node.key:
         node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
def deleteNode(root, key):
  
    # base case
    if root is None:
        return root

    # If the key to be deleted is smaller than the
    # root's key, then it lies in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # If the key to be deleted is greater than 
    # the root's key, then it lies in right subtree
    elif key > root.key:
        root.right = deleteNode(root.right, key)

    # if key is same as root's key
    else:
      
        # If key is present more than once, 
        # simply decrement count and return
        if root.count > 1:
            root.count -= 1
            return root

        # ELSE, delete the node

        # node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # node with two children: Get the inorder 
        # successor (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's 
        # content to this node
        root.key = temp.key
        root.count = temp.count

        # To ensure successor gets deleted by 
        # deleteNode call, set count to 0.
        temp.count = 0

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root

