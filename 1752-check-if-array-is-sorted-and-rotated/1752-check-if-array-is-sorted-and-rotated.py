class Solution:
    def check(self, nums: List[int]) -> bool:
        lis = sorted(nums)
        ind = 0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                continue
            elif nums[i]>nums[i+1]:
                ind = i+1
                break
        for i in range(len(lis)):
            if lis[i] == nums[ind]:
                ind = (ind+1)%len(lis)
            else:
                return False
        return True   
