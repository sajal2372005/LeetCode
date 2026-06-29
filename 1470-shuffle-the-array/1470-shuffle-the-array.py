class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        counter = 0
        for i in range((len(nums)//2)+1):
            if len(ans) == len(nums):
                break
            ans.append(nums[counter])
            counter = counter+n
            ans.append(nums[counter])
            counter = counter-(n-1)
        return ans
            


        