# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode):
#         dummy = ListNode(0)
#         dummy.next = head
#         prefix = 0
#         d = {0:dummy} 
#         while head:
#             prefix += head.val
#             d[prefix] = head
#             head = head.next

#         head = dummy
#         prefix = 0
#         while head:
#             prefix += head.val
#             head.next = d[prefix].next
#             head = head.next
        
#         return dummy.next
        value = []
        temp = head
        result = ListNode(0)
        temp2 = result
        def findZero(arr,val):
            n = m = len(arr)
            flg = True
            while flg:
                if m < 0:
                    flg =False
                if (sum(arr[m:n]) + val) == 0:
                    return m
                else: 
                    m -= 1
            return -1
        if head is None :
            return head
        elif head.next is None and head.val == 0:
            head = None
            return head
        while temp is not None:
            prev = value[len(value)-1] if len(value) > 0 else 0
            if (prev + temp.val) == 0 and temp.val != 0:
                value.pop()
            else:
                index = findZero(value,temp.val) 
                if index != -1:
                    value = value[:index]
                elif temp.val != 0:
                    value.append(temp.val)
            temp = temp.next
        for i in value:
            k = ListNode(i)
            result.next = k
            result = result.next
            
        return temp2.next
                
        