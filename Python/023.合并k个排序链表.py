# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 法1. 暴力法 O(nlogn) and O(n)
        # self.nodes = []
        # head = point = ListNode(0)
        # for i in lists:
        #     while i:
        #         self.nodes.append(i.val)
        #         i = i.next
        # for x in sorted(self.nodes):
        #     point.next = ListNode(x)
        #     point = point.next
        # return head.next
    
        # 法2. 分治法：化解成两个链表合并 O(kn) and O(1)
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    def merge(self, l, r):
        dummy = cur = ListNode(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next
