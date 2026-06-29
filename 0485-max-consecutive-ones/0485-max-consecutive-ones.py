class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        final = 0
        partial = 0
        partial1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                partial1 +=1
            if nums[i] == 0:
                partial = partial1
                partial1 = 0
                if final<partial:
                    final = partial
        if partial1>final:
            final = partial1
        return final