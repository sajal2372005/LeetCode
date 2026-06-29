class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = []
        for i in range(n+1):
            if i == 0:
                continue
            dic.append(i)
        matching = []
        non_match = []
        for i in range(len(nums)):
            if nums[i] not in non_match:
                non_match.append(nums[i])
                continue
            matching.append(nums[i])
        for i in range(len(nums)):
            if nums[i] in dic:
                dic.remove(nums[i])
        ans = matching+dic
        return ans

        