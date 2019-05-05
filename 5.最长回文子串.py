class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # 法1.暴力算法 O(n^3) O(n) 超出时限
        # lens = len(s)
        # if lens < 2:
        #     return s
        # maxlen = 0
        # start = 0
        # for i in range(lens):
        #     for j in range(i + 1, lens):
        #         begin = i
        #         end = j
        #         while begin <= end:
        #             if s[begin] != s[end]:
        #                 break
        #             else:
        #                 begin += 1
        #                 end -= 1
        #         if begin >= end and j - i +1 > maxlen:
        #             maxlen = j - i + 1
        #             start = i
        # if maxlen > 0:
        #     return s[start:maxlen+start]
        # return s[0]
        
        # 法 2.遍历字符串 O(n^2) 
#         res = ""
#         for i in range(len(s)):
#             # 奇数情况下：例如“aba”
#             tmp = self.helper(s, i, i)
#             if len(tmp) > len(res):
#                 res = tmp
                
#             # 偶数情况下：例如“abba”
#             tmp = self.helper(s, i, i+1)
#             if len(tmp) > len(res):
#                 res = tmp
#         return res
    
#     def helper(self, s, l, r):
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             l -= 1
#             r += 1
#         return s[l+1: r]
    
        # 法3.动态规划 O(n^2) O(n^2)
        # n = len(s)
        # maxlen = 1
        # if n < 2:
        #     return s
        # start = 0
        # dp = [[False for _ in range(n)] for i in range(n)]
        # for j in range(n):
        #     for i in range(j):
        #         dp[i][j] = (s[i] == s[j]) and (j - i < 2 or dp[i+1][j-1])
        #         if dp[i][j] and (maxlen < j - i + 1):
        #             maxlen = j -  i + 1
        #             start = i
        #     dp[j][j] = True
        # return s[start: start+maxlen]
        
        # 法4.manacher算法 O(n) and O(n)
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
        
    
            
