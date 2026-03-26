class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
def traverse(head):
  currentNode=head
  while currentNode:
    print(currentNode.data,end=" --> ")
    currentNode=currentNode.next
  print("null")
  
def minValue(head):
  if head is None:
    raise ValueError("empty")
    
  minvalue=head.data
  currentNode=head.next
  while currentNode:
    if currentNode.data < minvalue:
      minvalue=currentNode.data
    currentNode=currentNode.next
  return minvalue
  
def maxValue(head):
  maxValue=head.data
  currentNode=head.next
  while currentNode:
    if currentNode.data > maxValue:
      maxValue=currentNode.data
    currentNode=currentNode.next
  return maxValue

def delete(head,k):
  currentNode=head
  while currentNode:
    if currentNode.data==k:
      currentNode=currentNode.next
    print(currentNode.data,end=" -->")
    currentNode=currentNode.next


def delete(head,nodeTodelete):
  if head==nodeTodelete:
    return head.next
  currentNode=head
  while currentNode and currentNode.next != nodeTodelete:
    currentNode=currentNode.next
  if currentNode is None:
    return head
  currentNode.next=currentNode.next.next
  return head
  
def insert(head,newNode,postion):
  if postion==1:
    newNode.next=head
    return head
  currentNode=head
  for _ in range(postion-2):
    if currentNode is Node:
      break
    currentNode=currentNode.next
  newNode.next=currentNode.next
  currentNode.next=newNode
  return head
  

node1=Node(10)
node2=Node(2)
node3=Node(30)
node4=Node(1)
node5=Node(50)
 
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

traverse(node1)
print(minValue(node1))
print(maxValue(node1))
print(delete(node1,1))


def stack_linkedlist(stack):
  if not stack:
    head=None
    return head
  head=Node(stack.pop())
  current=head
  while stack:
    current.next=Node(stack.pop())
    current=current.next
  return head

stack = [10, 20, 30]
head=stack_linkedlist(stack)
traverse(head)


def length(head):
  count=0
  current=head
  while current:
    count=count+1
    current=current.next
  return count
# print(length(n1))
def linkedlist_stack(head):
  if not head:
    head=None
    return head
  stack=[]
  current=head
  while current:
    stack.append(current.data)
    current=current.next
  return stack 

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def is_empty(self):
        return self.front is None

class Queuedemo:
  def __init__(self,data):
    self.front=data
    self.rear=None
  def enqueue(self,data):
    new_node=Node(data)
    if self.rear is None:
      self.font=self.rear=new_node
      return new_node
    self.rear.next=new_node
    self.rear=new_node
  def dequeue(self):
    if self.font is None:
      print("queue is empty")
      return None
    remove=self.font
    self.font=self.font.next
    if self.font is None:
      self.rear=None
    return removed.data

class Node:
  def __init__(self, d):
    self.data = d
    self.next = None

# Function to reverse a linked list
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Function to check if two lists are identical
def isIdentical(n1, n2):
    while n1 and n2:
        if n1.data != n2.data:
            return False
        n1 = n1.next
        n2 = n2.next
    return True

# Function to check whether the list is palindrome
def isPalindrome(head):
    if head is None or head.next is None:
        return True

    slow, fast = head, head

    # Find the middle of the list
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Split the list and reverse the second half
    head2 = reverse(slow.next)
    slow.next = None

    # Check if the two halves are identical
    ret = isIdentical(head, head2)

    # Restore the original list
    head2 = reverse(head2)
    slow.next = head2

    return ret

if __name__ == "__main__":
  
    # Linked list : 1->2->3->2->1
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    result = isPalindrome(head)

    if result:
        print("true")
    else:
        print("false")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to check if the linked list 
# is palindrome or not
def isPalindrome(head):
    curr_node = head
    s = []

    # Push all elements of the list to the stack
    while curr_node is not None:
        s.append(curr_node.data)
        curr_node = curr_node.next

    # Iterate in the list again and check by'
    # popping from the stack
    while head is not None:
      
        # Get the topmost element
        c = s.pop()

        # Check if data is not same as popped element
        if head.data != c:
            return False

        # Move ahead
        head = head.next

    return True

# Linked list : 1->2->3->2->1
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

result = isPalindrome(head)

if result:
    print("true")
else:
    print("false")