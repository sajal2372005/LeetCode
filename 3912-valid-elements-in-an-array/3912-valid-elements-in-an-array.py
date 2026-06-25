class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        
        out = []
        if(len(nums)== 2):
            out.append(nums[0])
            out.append(nums[1])
            return out
        if(len(nums) == 1):
            return nums
        for i in range(len(nums)):
            left = True
            right = True

            for j in range(i - 1, -1, -1):  # check all elements to the left
                if nums[j] >= nums[i]:
                    left = False
                    break

            for j in range(i + 1, len(nums)):  # check all elements to the right
                if nums[j] >= nums[i]:
                    right = False
                    break

            if left or right:
                out.append(nums[i])

        return out