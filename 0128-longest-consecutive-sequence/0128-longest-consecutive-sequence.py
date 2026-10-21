class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sort = sorted(nums)

        if not nums:
            return 0
        longest = 1
        count = 1
        for i in range(len(sort)-1):
            if sort[i+1] - sort[i] == 1:
                count+=1
            elif sort[i+1] - sort[i] == 0:
                continue
            else:
                longest = max(longest,count)
                count = 1
        return max(longest,count)