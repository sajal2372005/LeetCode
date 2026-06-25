class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_list = {}
        lim = len(nums)/2
        for i in range(len(nums)):
            if nums[i] not in hash_list:
                hash_list[nums[i]] = 0
            hash_list[nums[i]] += 1

            if hash_list[nums[i]] > lim:
                return nums[i] 

        