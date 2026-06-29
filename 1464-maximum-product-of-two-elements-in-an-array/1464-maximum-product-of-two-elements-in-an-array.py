class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        small1=0
        small2=0
        c = 0
        if nums[0]<nums[1]:
            small1 = nums[0]
            small2 = nums[1]
        else:
            small1 = nums[1]
            small2 = nums[0]
            
        for i in range(len(nums)):
            if i == 0 or i == 1:
                continue
            if nums[i]>=small2:
                small1 = small2
                small2 = nums[i]
                c = i
            if nums[i]>small1 and i!=c:
                small1 = nums[i]
        small1-=1
        small2-=1
        return small1*small2
            

