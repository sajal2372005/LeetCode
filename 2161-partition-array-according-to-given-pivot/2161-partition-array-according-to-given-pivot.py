class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        more = []
        
        for i in range(len(nums)):
            if nums[i] == pivot:
                equal.append(nums[i])
            elif nums[i] < pivot:
                less.append(nums[i])
            elif nums[i]> pivot:
                more.append(nums[i])
        less = less+equal+more
        return less
