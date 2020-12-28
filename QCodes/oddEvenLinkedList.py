# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode):
        if head is None or head.next is None:
            return head
        temp = head
        temp2 = head.next
        counter = 1
        prev = None
        while temp.next is not None:
            temp1 = temp.next
            temp.next = temp.next.next
            prev = temp
            temp = temp1
            counter += 1
        # print(counter)
        if temp1 is not None:
            temp1.next = None
        if counter%2 != 0 :
            # print("None")
            temp.next = temp2
        else:
            # print("val")
            prev.next = temp2
        return head
            