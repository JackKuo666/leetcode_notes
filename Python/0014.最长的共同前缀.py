class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs: return ""
        ans = ""                 # strs = ["flower","flow","flight"]
        for i in zip(*strs):     # zip(*strs) = [(f,f,f),(l,l,l), (o,o,i), (w,w,g), (e,"",h), (r,"",t)]
            if len(set(i)) > 1: 
                break
            ans += i[0]
        return ans
