class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 法1. 加速减法
        """
        for example, if we want to calc (17/2)

            ret = 0;

            17-2 ,ret+=1; left=15

            15-4 ,ret+=2; left=11

            11-8 ,ret+=4; left=3

            3-2 ,ret+=1; left=1

            ret=8;
        """
        
        if dividend == 0:
            return 0

        
        flag1 = 1
        if dividend < 0 :
            dividend = 0 - dividend
            flag1 = -1
        
        flag2 = 1
        if divisor < 0:
            divisor = 0 - divisor
            flag2 = -1
        
        count = 0
        while dividend >= divisor:
            tmp, val = divisor, 1
            while dividend >= tmp:
                count += val
                dividend -= tmp
                tmp += tmp
                val += val
        if (flag1 < 0) ==  (flag2 < 0):
            return min(count, 2147483647)
        else:
            return max(0 - count, -2147483648)
