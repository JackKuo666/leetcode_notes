# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        i = 0
        while l1:
            num1 += l1.val * (10**i)
            i += 1
            l1 = l1.next
        
        num2 = 0
        i = 0
        while l2:
            num2 += l2.val * (10**i)
            i += 1
            l2 = l2.next
        
        suml = num1 + num2
        
        ans = ListNode(0)
        temp = ans
        for i in str(suml)[::-1]:
            temp.next = ListNode(i)
            temp = temp.next
        return ans.next
