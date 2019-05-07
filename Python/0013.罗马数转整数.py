class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # M = ["", "M", "MM", "MMM"]                                           # 0 1000 2000 3000
        # C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]     # 0 100 200 300 400 500 ... 900
        # X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]     # 0 10 20 ... 90
        # I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]     # 0 1 2 3 ... 9
        
        # 自典法
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII") # 4   9    不是累加的
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX") # 40  90  不是累加的
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC") # 400 900 不是累加的
        for char in s:
            number += translations[char]
        return number
        
