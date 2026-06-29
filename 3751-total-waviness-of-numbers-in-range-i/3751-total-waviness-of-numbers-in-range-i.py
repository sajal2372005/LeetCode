class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        ans = 0
        for i in range(num1,num2+1):
            i = str(i)
            for s in range(1,len(i)-1):
                if (i[s] > i[s-1] and i[s]>i[s+1]) or (i[s] < i[s-1] and i[s]<i[s+1]):
                    ans+=1
        return ans