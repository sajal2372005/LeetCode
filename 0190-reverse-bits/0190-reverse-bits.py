class Solution:
    def reverseBits(self, n: int) -> int:
        queue = []
        final = ""
        bi = f'{n:b}'
        if len(bi) < 32:
            temp = 32 - len(bi)
            bi = "0"*temp + bi
        for i in range(len(bi)-1,-1,-1):
            final += bi[i]
        ans = int(final,2)
        return ans
        