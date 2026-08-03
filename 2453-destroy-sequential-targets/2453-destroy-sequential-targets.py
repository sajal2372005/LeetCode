class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums = sorted(nums)
        dict = {}
        for i in range(len(nums)):
            rem = nums[i]%space
            if rem not in dict:
                dict[rem] = 1
            else:
                dict[rem]+=1
        maxi = max(dict.values())
        ans = float('inf')
        for i in range(len(nums)):
            rem = nums[i] % space
            if dict[rem] == maxi:
                
                if nums[i] < ans:
                    ans = nums[i]
                    
        return ans