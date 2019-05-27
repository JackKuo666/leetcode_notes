class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 法1. O(nk) and O(1)
        s = '1'                               # 将第一行的1换成字符类型，便于下一行的读出
        for _ in range (n-1):                 # (n-1)是因为第一行不需要处理，直接可以读出
            i, tmp, count = s[0], '', 0       # i用来读取上一行的每一个字符，tmp用来存放读出的内容(char)，count用来统计
            for j in s:   
                if i == j:
                    count += 1
                else:
                    tmp += str(count) + i   
                    i = j
                    count = 1
            tmp += str(count) + i
            s = tmp
        return s
