class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # final = []
        # nums.sort()
        # for x in range(len(nums)):
        #     for i in range(x+1,len(nums)):
        #         for j in range(i+1,len(nums)):
        #             if x != i and x != j and i != j:
        #                 if nums[x]+nums[i]+nums[j] == 0:
        #                     if [nums[x],nums[i],nums[j]] not in final:
        #                         final.append([nums[x],nums[i],nums[j]])
        # return final
        sets = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            for j in range(i+1,len(nums)):
                if left >= right:
                    break
                if i!=left and i!= right and left != right:
                    if nums[i]+nums[left]+nums[right] == 0:
                    
                        sets.add((nums[i],nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif nums[i]+nums[left]+nums[right] > 0:
                        right -=1
                    elif nums[i]+nums[left]+nums[right] < 0:
                        left +=1
        return [list(triplet) for triplet in sets]