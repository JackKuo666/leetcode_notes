class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ans = ""
        digit = "0123456789"
        str = str.strip()
        
        if not str or str[0] not in "-+" + digit:
            return 0
        
        flag = 0
        if str[0] == "-":
            flag = -1
            str = str[1:]
            ans += "-"
        elif str[0] == "+":
            flag = 1
            str = str[1:]
        for i in str:
            if i in digit:
                ans += i
            else:
                break
        
        if ans == "-" or ans == "":
            return 0
        return  max(int(ans), -2**31) if flag == -1 else min(int(ans), 2**31 -1)
                
            
        
        
