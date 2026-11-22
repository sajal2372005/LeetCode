class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            if len(nums) % (i+1) == 0:
                arr.append(nums[i])
        final = 0
        for i in arr:
            final += i*i
        return final