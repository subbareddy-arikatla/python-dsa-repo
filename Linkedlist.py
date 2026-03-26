class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(5)
b = Node(7)
c = Node(2)

a.next = b
b.next = c

head = a

print(head.data)              # 5
print(head.next.data)         # 7
print(head.next.next.data)    # 2

def printLL(head):
    curr=head
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.next

a = Node(5)
b = Node(7)
c = Node(2)

a.next = b
b.next = c

head = a

# printLL(head)

# insert at the eginning

newNode=Node(4)
newNode.next=head
head=newNode
# printLL(head)

lastnewNode=Node(10)
lastnewNode.next=None
c.next=lastnewNode
printLL(head)

# insert at kth index
newNode=Node(6)
k=4
curr=head
for i in range(k-2):
    curr=curr.next
newNode.next=curr.next
curr.next=newNode

# remove the first node 
head=head.next
printLL(head)

# remove the last NODE

curr=head
while curr.next.next != None:
    curr=curr.next
curr.next=newNode

k=3
curr=head
for i in range(k=2):
    curr=curr.next
curr.next=curr.next.next
printLL(head)


    