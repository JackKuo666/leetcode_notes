class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 法1.动态规划 O(n) and O(1)
        # dp, res = [0] * len(s), 0
        # for i in range(len(s)):
        #     if s[i] == ")":
        #         if i > 0 and s[i - 1] == "(":
        #             dp[i] = dp[i - 2] + 2
        #         if i > 0 and s[i - 1] == ")":
        #             if i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
        #                 if i - dp[i - 1] - 1 > 0:
        #                     dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        #                 else:
        #                     dp[i] = dp[i - 1] + 2
        #         res = max(res, dp[i])
        # return res
        
        # 法2.stack法 O(n) and O(1)
        stack, res = [-1], 0
        for i, e in enumerate(s):
            if e == "(":
                stack.append(i)
            if e == ")":
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
                
