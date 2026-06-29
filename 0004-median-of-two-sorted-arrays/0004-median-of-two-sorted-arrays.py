class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1+nums2)
        n = len(merged)

        if n%2 == 1:
            median = merged[n//2]
            return float(median)
        else:
            ind1 = n//2
            ind2 = ind1-1
            return (merged[ind1]+merged[ind2])/2