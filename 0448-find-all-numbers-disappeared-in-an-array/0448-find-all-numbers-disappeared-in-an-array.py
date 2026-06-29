class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lis = set(nums)
        ans = []
        for i in range(n+1):
            if i == 0:
                continue
            if i not in lis:
                ans.append(i)
        return ans