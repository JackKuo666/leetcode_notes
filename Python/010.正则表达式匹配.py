class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 法1.内置函数
        # return re.match('^' + p + '$', s) != None

        # 法2.递归  
#         lens, lenp= len(s), len(p)
        
#         # 其中一个为空
#         if lens == 0 and lenp == 0:
#             return True
#         elif lens != 0 and lenp == 0:
#             return False
#         elif lens == 0 and lenp != 0:
#             if lenp > 1 and p[1] == "*":
#                 return self.isMatch(s, p[2:])
#             else:
#                 return False
        
#         # 两个都不为空
#         else:
#             # p[1] 为*
#             if lenp > 1 and p[1] == "*":
#                 if s[0] != p[0] and p[0] != ".":
#                     return self.isMatch(s, p[2:])
#                 else:
#                     return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p)
#             # p[1] 不为*
#             else:
#                 if s[0] == p[0] or p[0] == ".":
#                     return self.isMatch(s[1:], p[1:])
#                 else:
#                     return False
        
    
        # 法3.dp    
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]
        
