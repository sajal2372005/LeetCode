class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = n
            digit = 1
            while temp>0:
                digit *= temp%10
                temp //= 10
            if digit%t == 0:
                return n
            n+=1