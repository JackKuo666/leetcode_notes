class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 法1.数组法 O(n*4^(n+1)) and O(n)
        if digits == "":
            return []
        dic = ["","","abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [""]
        for i in digits:
            temp = []
            for j in dic[int(i)]:
                for k in ans:
                    temp.append(k+j)
            ans = temp
        return ans
        
#         # 法2.回溯法 > O(n*4^(n+1)) and O(n)
#         dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

#         if len(digits) < 1:
#             return ""
#         if len(digits) == 1:
#             return [i for i in dic[digits]]

#         res = []
#         for i in range(len(digits)):
#             for j in dic[digits[i]]:
#                 for k in self.letterCombinations(digits[i+1:]):
#                     res.append(j + k)
#         return [i for i in res if len(i) == len(digits)]
