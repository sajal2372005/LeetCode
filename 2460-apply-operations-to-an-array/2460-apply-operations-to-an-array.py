class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        result = [0]*len(nums)
        current = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                result[current] = nums[i]
                current+=1
            i+=1
            
        return result 
        