# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int):
        temp = head
        less = []
        higher = []
        while temp is not None:
            if temp.val < x:
                less.append(temp.val)
            else:
                higher.append(temp.val)
            temp = temp.next

        res = ListNode(0)
        ans = res
        for i in less:
            k = ListNode(i)
            res.next = k
            res = res.next
        for j in higher:
            m = ListNode(j)
            res.next = m
            res = res.next
        
        return ans.next