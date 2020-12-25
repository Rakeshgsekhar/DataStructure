# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) :
        num = []
        temp = head
        isPalin = True
        # if head is not None and head.next is None:
        #     return True
        while temp is not None:
            num.append(temp.val)
            temp = temp.next
        
        while head is not None:
            stackVal = num.pop()
            
            if head.val == stackVal:
                isPalin = True
            else:
                isPalin = False
                break
            head = head.next
        return isPalin