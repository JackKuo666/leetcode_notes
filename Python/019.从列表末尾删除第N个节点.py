# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 法1.数组法两边遍历 O(n^2) and O(n)
#         res = []
#         while head:
#             res.append(head.val)
#             head = head.next
#         res = res[:-n] +  (res[-n+1:] if -n+1 < 0 else [])
#         ans = ListNode(0)
#         tmp = ans
#         for i in res:
#             tmp.next = ListNode(i)
#             tmp = tmp.next
#         return ans.next
    
#         # 法2.递归法
#         def index(node):
#             if not node:
#                 return 0
#             i = index(node.next) + 1      # 由于是递归法，所以i是从最后一个往前加的
#             if i > n:
#                 node.next.val = node.val  # 没有删除倒数第n个listnode，而是将值后移了
#             return i
#         index(head)
#         return head.next
    
       # 法3.快慢指针
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next          # 快指针剩余的个数 （总个数-n） 刚好是慢指针需要走的个数
            slow = slow.next
        slow.next = slow.next.next
        return head
