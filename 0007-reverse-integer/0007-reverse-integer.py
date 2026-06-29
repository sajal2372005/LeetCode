class Solution:
    def reverse(self, x: int) -> int:
        
        if x<0:
            lis = [d for d in str(x)]
            lis.remove('-')
            lis1 = [int(d) for d in lis]
            lis2 = lis1[::-1]
            string = "".join(map(str,lis2))
            num = int(string)
            if num>2**31:
                return 0
            result = 0-num
            return result
        lis = [int(d) for d in str(x)]
        lis1 = lis[::-1]
        string = "".join(map(str,lis1))
        num = int(string)
        if num > 2**31 - 1:
            return 0
        return num
