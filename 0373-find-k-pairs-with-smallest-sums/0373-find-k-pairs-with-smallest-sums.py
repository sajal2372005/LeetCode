import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
            
        min_heap = []
        ans = []
        
        # Step 1: Only push the first 'k' combinations using the first element of nums2.
        # Format: (sum, nums1_index, nums2_index)
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
            
        # Step 2: Pop the smallest, and push the next possible pair for that specific nums1 element
        while min_heap and len(ans) < k:
            current_sum, i, j = heapq.heappop(min_heap)
            
            # Add the actual pair to the answer
            ans.append([nums1[i], nums2[j]])
            
            # If there is another element in nums2, pair it with nums1[i] and push to heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return ans