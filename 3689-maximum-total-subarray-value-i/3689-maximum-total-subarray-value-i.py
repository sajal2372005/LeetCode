class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minimum = min(nums)
        maximum = max(nums)
        ans = maximum-minimum
        return ans*k

        