class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def reverseinorder(root,count,result):
    if root is None or count[0]>=2:
        return
    reverseinorder(root.right,count,result)
    count[0]+=1
    if count[0]==2:
        result[0]=root.data
        return
    reverseinorder(root.left,count,result)


def findSecondLargest(root):
    count = [0]  
    result = [-1] 

    # Start reverse inorder traversal
    reverseinorder(root, count, result)

    return result[0] 

if __name__ == "__main__":
    
    # Representation of the input BST:
    #              7
    #             / \
    #            4   8
    #           / \   
    #          3   5 
    root = Node(7)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(3)
    root.left.right = Node(5)

    secondLargest = findSecondLargest(root)

    print(secondLargest) 