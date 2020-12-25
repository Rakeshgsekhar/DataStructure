# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode):
        counter = 0
        temp = head
        res = 0
        while temp.next is not None:
            counter += 1
            temp = temp.next
        # print(counter)
        while head is not None:
            # print(2** counter)
            res =res + (2 **counter) * head.val
            counter -= 1
            head = head.next
        
        return res