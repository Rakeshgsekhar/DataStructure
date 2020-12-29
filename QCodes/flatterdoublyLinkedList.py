"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node'):
        
        if head is None:
            return head
        temp = head
        stack = [head]
        prev =Node(0)
        val = []
        while stack:
            # val.append(temp.val)
            # if temp.child is not None:
            #     stack.append(temp.next)
            #     # prev = temp
            #     temp = temp.child
            #     # temp.prev = prev
            # elif temp.next is None and len(stack) > 0:
            #     temp = stack.pop()
            #     # temp.prev = prev
            # else:
            #     temp = temp.next
            root = stack.pop()
            root.prev = prev
            prev.next = root
            prev = root
            if root.next:
                stack.append(root.next)
            if root.child:
                stack.append(root.child)
                root.child = None
            
        head.prev = None
            
        return head
#         if not head:
#             return 
#         stk=[head]
#         prev=Node(0)
#         while stk:
#             root=stk.pop()
#             root.prev=prev
#             prev.next=root
#             prev=root
#             if root.next:
#                 stk.append(root.next)
#             if root.child:
#                 stk.append(root.child)
#                 root.child=None
                
#         head.prev=None
#         return head
        