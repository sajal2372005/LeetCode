class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    nums[j],nums[i] = nums[i],nums[j]
        return nums