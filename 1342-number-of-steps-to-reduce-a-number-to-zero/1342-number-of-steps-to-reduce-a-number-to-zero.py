class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num >= 1:
            if num%2 == 0:
                num = num/2
            else:
                num -=1
            count+=1
        return count
