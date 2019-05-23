# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 法1. 一行替换
        """
        Here, pre is the previous node. Since the head doesn't have a previous node, I just use self instead. Again, a is the current node and b is the next node.

To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references. Instead of thinking about in what order I change them, I just change all three at once.
        """
        tmp = ListNode(0)
        pre, pre.next = tmp, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return tmp.next
        
