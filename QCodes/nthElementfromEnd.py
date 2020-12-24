
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        temp = head
        prev = None
        counter = 0
        if head is None:
            return
        if head.next is None and n == 1:
            head = None
            return
        # if n == 2:
            
        while temp is not None:
            counter += 1
            temp = temp.next

        k = counter-n
        # print(k)
        if k == 0:
            head = head.next
            return head
        
        temp1 = head
        for i in range(k):
            prev = temp1
            temp1 = temp1.next
        
        prev.next = temp1.next
        
        return head