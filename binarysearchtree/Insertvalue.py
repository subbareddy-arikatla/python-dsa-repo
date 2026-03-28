def insert(root,key):
    if root is None:
        return Node(key)
    
    if key<root.data:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root

def insert(root,key):
    temp=Node(key)
    if root is None:
        root=temp
    curr=temp
    while curr is not None:
        if curr.data>key and curr.left is not None:
            curr=curr.left
        elif curr.data<key and curr.right is not None:
            curr=curr.right
        break
    if curr.data>key:
        curr.left=temp
    else:
        curr.right=temp
    return root