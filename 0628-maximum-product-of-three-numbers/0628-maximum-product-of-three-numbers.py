class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        first = nums[n-1] * nums[n-2] * nums[n-3]
        sec = nums[0]*nums[1]*nums[n-1]
        return max(first,sec)