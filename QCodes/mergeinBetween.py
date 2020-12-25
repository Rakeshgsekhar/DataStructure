# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode):
        counter = 0
        temp = list1
        prev = None
        while counter < a:
            prev = temp
            temp = temp.next
            counter += 1
        sec = temp.next
        prev.next = list2
        prev1 = None
        while counter <= b:
            prev1 = sec
            sec = sec.next
            counter += 1
        
        while prev.next is not None:
            prev = prev.next
        prev.next = prev1
        
        return list1