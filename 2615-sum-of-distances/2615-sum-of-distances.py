class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # arr = []
        # for i in range(len(nums)):
        #     temp = nums[i]
        #     sum = 0
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         elif nums[j] == temp:
        #             sum += abs(i-j)
        #     arr.append(sum)
        # return arr
                
        # dic = {}
        # for i in range(len(nums)):
        #     if nums[i] not in dic:
        #         dic[nums[i]] = []
        #     dic[nums[i]].append(i)
        # arr = []
        # for i in range(len(nums)):
        #     temp = dic[nums[i]]
        #     sum = 0
        #     for j in range(len(temp)):
        #         if i == temp[j]:
        #             continue
        #         else:
        #             sum += abs(i-temp[j])
        #     arr.append(sum)
        # return arr


        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = []
            dic[nums[i]].append(i)
        
        arr = [0] * len(nums)
        
        for val, idxs in dic.items():
            k = len(idxs)
            # total distance from idxs[0] to all others (sum of i - idxs[0] for i in idxs[1:])
            total = sum(idxs) - idxs[0] * k
            
            # left_count/left_sum track the group already "passed"
            prev = idxs[0]
            left_count = 0
            left_sum = 0
            
            for i in range(k):
                cur = idxs[i]
                gap = cur - prev
                # moving from prev to cur:
                # everything on the left side gets +gap each (left_count of them)
                # everything on the right side gets -gap each (k - left_count of them, excluding self)
                total += left_count * gap - (k - left_count) * gap
                
                arr[cur] = total
                
                left_sum += cur
                left_count += 1
                prev = cur
        
        return arr