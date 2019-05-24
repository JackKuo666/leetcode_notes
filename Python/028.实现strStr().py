class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 法1. O(nk) and O(1)
        if not needle:
            return 0
        if not haystack:
            return -1

        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i+len(needle) <= len(haystack):
                    if haystack[i : i+len(needle)] == needle:
                        return i
        return -1
