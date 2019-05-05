   def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1): return s
        a = [[]for i in range(numRows)]#产生一个有numrows单元的list，每个list可以在后面添加元素
        r = 0
        direct = 1 #行前进的方向是向上还是向下
        for c in s:
            a[r].append(c)
            if r >= numRows-1:
                direct = -1
            elif r == 0:
                direct = 1
            r += direct
        answer = ""
        for row in a:#按行优先打印出来
            for col in row:
                answer += col
        return answer
