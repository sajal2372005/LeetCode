class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = 0
        maxi2 = 0
        for i in range(len(nums)):
            if nums[i]>maxi2:
                maxi2 = nums[i]
            if maxi < maxi2:
                temp = maxi
                maxi = maxi2
                maxi2 = temp
        return ((maxi-1)*(maxi2-1))
        