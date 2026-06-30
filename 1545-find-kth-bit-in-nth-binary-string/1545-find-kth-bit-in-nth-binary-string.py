class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def reverse(s:str):
            return s[::-1]
        def invert(s:str):
            string = ""
            for i in range(len(s)):
                
                if s[i] == "0":
                    string += '1'
                if s[i] == '1':
                    string += '0'
            return string
        left = "0"
        
        for i in range(n):
            if i == 0:
                continue
            left = left + "1" + reverse(invert(left))
        return left[k-1]