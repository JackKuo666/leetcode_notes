# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 法1.暴力循环 O(3N) and O(n) 
#         list_ = []
#         while head:
#             list_.append(head.val)
#             head = head.next
        
#         li = []
#         tm = []
#         for i in range(len(list_)):
#             tm.append(list_[i])
#             if (i+1) % k == 0:
#                 li += tm[::-1]
#                 tm = []
#         li += tm 
        
#         ans = tmp = ListNode(0)
#         for i in li:
#             tmp.next = ListNode(i)
#             tmp = tmp.next
        
#         return ans.next
            
        # 法2.迭代法 O(n) and O(1)
        # https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next
                
            
        
