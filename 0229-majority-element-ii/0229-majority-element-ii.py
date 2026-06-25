class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lim = len(nums)//3
        dic = {}
        lis = []
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 0
            dic[nums[i]]+=1

        for num in dic:
            if dic[num] > lim:
                lis.append(num)
        return lis
                
        