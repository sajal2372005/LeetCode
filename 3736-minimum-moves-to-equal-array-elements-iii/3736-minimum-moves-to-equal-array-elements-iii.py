class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        cost = 0
        for i in range(len(nums)):
            if nums[i] < maxi:
                cost += maxi - nums[i]
            else:
                continue
        return cost
        