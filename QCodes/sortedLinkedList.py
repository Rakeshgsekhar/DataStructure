# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode):
        def getMiddleNode(node):
            if (node == None): 
                return node 
            slow = node 
            fast = node 
            while (fast.next != None and 
                   fast.next.next != None): 
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def sortedMerge(a,b):
            result = None 
            if a == None: 
                return b 
            if b == None: 
                return a  
            if a.val <= b.val: 
                result = a 
                result.next = sortedMerge(a.next, b) 
            else: 
                result = b 
                result.next = sortedMerge(a, b.next) 
            return result
        
        if head == None or head.next == None: 
            return head
  
        middle = getMiddleNode(head) 
        nexttomiddle = middle.next
 
        middle.next = None

        left = self.sortList(head) 
     
        right = self.sortList(nexttomiddle) 

        sortedlist = sortedMerge(left, right) 
        return sortedlist 
            