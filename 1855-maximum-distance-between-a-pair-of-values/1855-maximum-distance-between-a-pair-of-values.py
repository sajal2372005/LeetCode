from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        max_dist = 0
        
        while i < len(nums1) and j < len(nums2):
            # If valid, calculate distance and expand the window by moving j
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            # If invalid, nums1[i] is too big, move i to get a smaller value
            else:
                i += 1
                
        return max_dist