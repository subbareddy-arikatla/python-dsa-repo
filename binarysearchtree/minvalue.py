def minValue(root):
    if root.left is None:
        return root.data
    return minValue(root.left)
def minValue(root):
    if root is None:
        return -1
    curr=root
    while curr.left is not None:
        curr=curr.left
    return curr.data