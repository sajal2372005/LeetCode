class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        l = len(nums)-1
        if nums[len(nums)-1]!=l:
            return False

        j = 1
        for i in range(len(nums)):
            if j==len(nums):
                j = j
                continue
            if j!=nums[i]:
                return False
            if j==nums[i]:
                j = j+1
        

        return True
        