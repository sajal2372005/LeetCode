class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        sets = set(nums)
        output = []
        for i in range(nums[0],nums[len(nums)-1]):
            if i not in sets:
                output.append(i)

        return output
