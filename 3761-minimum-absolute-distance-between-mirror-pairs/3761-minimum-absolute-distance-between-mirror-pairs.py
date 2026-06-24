from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # Dictionary to store {expected_mirror_value: index_where_we_saw_it}
        seen_mirrors = {}
        min_dist = float('inf') # Start with infinity so any real distance is smaller

        # enumerate gives us both the index (j) and the value (num) at the same time
        for j, num in enumerate(nums):
            
            # 1. Did a previous number need THIS number as its mirror?
            if num in seen_mirrors:
                # The distance is the current index (j) minus the old index
                dist = j - seen_mirrors[num]
                if dist < min_dist:
                    min_dist = dist
            
            # 2. What mirror does the CURRENT number need?
            # We calculate it once and store it in our dictionary
            mirror_val = int(str(num)[::-1])
            
            # We save/overwrite the index in the dictionary. 
            # If we see the same mirror requirement twice, we want to keep the 
            # latest index (j) because it will result in a smaller distance later!
            seen_mirrors[mirror_val] = j

        # If min_dist is still infinity, we never found a pair, so return -1
        return min_dist if min_dist != float('inf') else -1