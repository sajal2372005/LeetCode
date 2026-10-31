class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k =-1
        for i in range(len(nums)):
            if nums[i] != i:
                if k == -11:
                    k = nums[i]
                else:
                    k &= nums[i]
        return k if k != -1 else 0