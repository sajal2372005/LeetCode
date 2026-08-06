class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total = 0
        pre = 0
        for char in reversed(s):
            temp = roman[char]
            if temp >= pre:
                total += temp
            else:
                total -= temp
            pre = temp
        return total