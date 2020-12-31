class Solution:
    def swapPairs(self, head: ListNode):
        if head is None or head.next is None:
            return head
        tempx = ListNode(0)
        tempx.next = head
        temp2 = tempx
        while tempx.next is not  None and tempx.next.next is not None:
            first = tempx.next
            sec = tempx.next.next
            tempx.next = sec
            first.next = sec.next
            sec.next = first
            tempx = tempx.next.next
        return temp2.next