class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 法1.字典法 O(n) and O(n)
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
        
