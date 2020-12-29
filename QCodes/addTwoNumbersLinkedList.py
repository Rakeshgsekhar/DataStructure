# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) :
        stack1 = []
        stack2 = []
        resultStack = []
        carryOver = 0
        result = ListNode(0)
        if l1 is None and l2 is None:
            return l1
        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next
        
        while len(stack1) > 0 and len(stack2)>0:
            a = stack1.pop()
            b = stack2.pop()
            sm = a + b + carryOver
            if sm>9:
                carryOver = sm//10
                sm = sm%10
            else:
                carryOver = 0
            resultStack.append(sm)
        print(carryOver)
        if len(stack1)>0:
            while len(stack1)>0:
                k = stack1.pop()+carryOver
                if k > 9:
                    carryOver = k//10
                    k = k%10
                else:
                    carryOver = 0
                resultStack.append(k)
        
        
        if len(stack2)>0:
            while len(stack2)>0:
                k = stack2.pop()+carryOver
                if k > 9:
                    carryOver = k//10
                    k = k%10
                else:
                    carryOver = 0
                
                resultStack.append(k)
        if carryOver > 0:
            resultStack.append(carryOver)
        head = result
        while len(resultStack) > 0 :
            result.next = ListNode(resultStack.pop())
            result = result.next
        return head.next



        ##
        # 
        # class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     one = 0
    #     two = 0
        
    #     while l1 or l2:
    #         if l1:
    #             one = one*10 + l1.val
    #             l1 = l1.next
    #         if l2:
    #             two = two*10 + l2.val
    #             l2 = l2.next
        
    #     sm = str(one+two)
    #     f = head = ListNode(0)
        
    #     for i in sm:
    #         head.next = ListNode(int(i))
    #         head = head.next
    #     return f.next
    #     # 
        # 
        # ##
