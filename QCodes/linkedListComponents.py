# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]):
        counter = 0
        temp = head
        memo = []
        connected =[]
        while temp is not None:
            if temp.val in G and temp.val not in connected:
                connected.append(temp.val)
                if temp.next is not None and temp.next.val in G:
                    connected.append(temp.next.val)
                else:
                    memo.append(connected)
                    counter += 1
                    connected = []
            elif temp.val in connected:
                if temp.next is not None and temp.next.val in G:
                    connected.append(temp.next.val)
                else:
                    memo.append(connected)
                    counter += 1
                    connected = []
            temp = temp.next
        # print (memo)
        return counter
        