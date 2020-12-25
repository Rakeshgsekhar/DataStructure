class Solution:
    def mergeTwoLists(self, l1, l2):
        l3 = ListNode(0)
        temp = l3
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
            
        if l1 is not None:
            temp.next = l1
        if l2 is not None:
            temp.next = l2
            # l2 = l2.next
        # print(l3)    
        return l3.next