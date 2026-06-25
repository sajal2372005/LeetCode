class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        smallest = nums[0]
        for i in range((len(nums)//2)+1):
            if nums[left]<nums[right] and nums[left]<smallest:
                smallest = nums[left]
            if nums[right]<nums[left] and nums[right]<smallest:
                smallest = nums[right]
            if nums[right] == nums[left] and nums[right]<smallest:
                smallest = nums[right]
            right -=1
            left +=1
        return smallest
                

        