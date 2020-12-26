class Solution:
    def nextLargerNodes(self, head: ListNode):
        res,stack = [],[]
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append([len(res), head.val])
            res.append(0)
            head = head.next
            
        return res

        ##
        # pos = -1
        # stack = []
		# ans = []
		# while head:
        #     pos += 1
		# 	ans.append(0)
		# 	while stack and stack[-1][1] < head.val:
        #         idx, _ = stack.pop()
        #         ans[idx] = head.val
		# 	stack.append((pos, head.val))
        #     head = head.next
        # return ans
        # ###