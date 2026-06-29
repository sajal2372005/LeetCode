class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        minimum = 5000
        for i in range((len(nums)//2)+1):
            if nums[left]<nums[right] and nums[left]<minimum:
                minimum = nums[left]

            if nums[right]<nums[left] and nums[right]<minimum:
                minimum = nums[right]
            if nums[left] == nums[right] and nums[right]<minimum:
                minimum = nums[right]
            right -=1
            left +=1
        return minimum
