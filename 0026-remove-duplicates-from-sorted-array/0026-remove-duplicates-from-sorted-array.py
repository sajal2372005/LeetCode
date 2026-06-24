class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = -101
        num2 = []
        for i in range(len(nums)):
            if(nums[i]!=num):
                num2.append(nums[i])
                num = nums[i]
        for i in range(len(num2)):
            nums[i]=num2[i]
        return len(num2)
