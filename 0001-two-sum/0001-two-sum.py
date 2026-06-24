class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]]=i
        
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in dic and (dic[compliment] != i):
                return [i,dic[compliment]]