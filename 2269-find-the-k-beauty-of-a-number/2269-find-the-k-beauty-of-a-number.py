class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        snum = str(num)
        count = 0
        for i in range(len(snum)-k+1):
            sub = snum[i:i+k]
            sub = int(sub)
            if sub != 0 and num % sub == 0:
                count+=1
        return count


        