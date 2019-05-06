class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 法1.str法+abs  36ms
        # ans = int(str(abs(x))[::-1]) if abs(x) == x else -1 * (int(str(abs(x))[::-1]))
        # if ans < -2**31 or ans > pow(2, 31) : 
        #     return 0
        # else:
        #     return ans
        
        # 法2.不用abs的str法  24ms
        # s = str(x)
        # ans = int(("-" + s[1:][::-1]) if s[0] == "-" else s[::-1])
        # return ans if -2**31 <= ans <= 2**31 else 0
        
        # 法3.除法 24ms
        y = x if x > 0 else -x
        ans = 0
        while y:
            ans = ans * 10 + y%10
            y /= 10
        
        return (ans if x > 0 else -1*ans) if -2**31 <= ans <= 2**31 else 0
