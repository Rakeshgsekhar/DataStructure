class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printMiddleElement(head):
    temp = head
    temp1 = head
    if temp is None:
        print ('No Elements Found')
    count = 0
    while temp is not None:
        count += 1
        temp = temp.next
    
    mid = count//2 + 1

    for i in range(1,mid):
        temp1 = temp1.next
    
    print(temp1.data)


l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l5 = Node(5)
l6 = Node(6)
l7 = Node(7)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7

head = None
head = l1

printMiddleElement(head)
