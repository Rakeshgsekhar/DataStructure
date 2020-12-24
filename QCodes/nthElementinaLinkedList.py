class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def findNthElement(head,position):
    temp = head
    if position == 0:
        return temp.data
    for i in range(position):
        temp = temp.next
        if temp is None:
            return "Position Exceeds List Length"
    
    if temp is None:
        return "Position Exceeds List Length"
    
    return temp.data



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

print (findNthElement(head,3))
