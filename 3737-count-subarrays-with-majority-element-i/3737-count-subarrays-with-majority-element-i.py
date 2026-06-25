class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # arr = []
        # ans = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         arr.append(nums[i:j+1])
        # for i in range(len(arr)):
        #     count=0
        #     for j in range(len(arr[i])):
        #         if arr[i][j] == target:
        #             count+=1
        #     temp = (count/len(arr[i]))
        #     if temp > 0.5:
        #         ans+=1
        # return ans

        # ans = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         temp = nums[i:j+1]
        #         total = temp.count(target)
        #         if total/len(temp) > 0.5:
        #             ans+=1
        # return ans

        ans = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                if nums[j] == target:
                    count+=1
                
                length = j-i+1
                if count/length > 0.5:
                    ans +=1
        return ans
