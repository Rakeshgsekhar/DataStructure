class Solution:
    def reverseList(self, head):
        
#         if head is None or head.next is None:
#             return head
#         rev = self.reverseList(head.next)
        
#         head.next.next = head.next
#         head.next = None
        
#         return rev
        prev = None
        current = head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        
        return head