from typing import List
import collections
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # 1. Precompute the locations of all numbers
        # index_map will look like: { number: [index1, index2, ...] }
        index_map = collections.defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)
            
        out = []
        n = len(nums)
        
        for q in queries:
            num = nums[q]
            indices = index_map[num]
            
            # 2. If the number only appears once, there are no duplicates
            if len(indices) == 1:
                out.append(-1)
                continue
                
            # 3. Use binary search to find the position of our query index (q) 
            # inside the 'indices' list.
            pos = bisect.bisect_left(indices, q)
            
            # 4. The closest identical numbers are exactly one spot to the left 
            # and right in the indices list. 
            # We use modulo to wrap around in case 'q' is at the very beginning or end.
            left_idx = indices[(pos - 1) % len(indices)]
            right_idx = indices[(pos + 1) % len(indices)]
            
            # 5. Calculate the circular distances
            left_dist = (q - left_idx + n) % n
            right_dist = (right_idx - q + n) % n
            
            # Append the shortest distance
            out.append(min(left_dist, right_dist))
            
        return out