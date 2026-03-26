# https://medium.com/javarevisited/15-leetcode-problems-to-get-better-at-linked-list-4c5aa8cd4a11

class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None

def print_list(head):
    ptr = head
    while ptr is not None:
        print(f"({ptr.key}, {ptr.data})")
        ptr = ptr.next

# create nodes
node1 = Node(10, 1)
node2 = Node(20, 2)
node3 = Node(30, 3)
node4 = Node(40, 4)
node5 = Node(50, 5)

# link nodes
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node5

node5.prev = node4

# head of the list
head = node1

# print list
print_list(head)
