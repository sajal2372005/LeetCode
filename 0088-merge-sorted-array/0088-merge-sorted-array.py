class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        l = 0
        r = 0
        for i in range(len(nums1)):
            if r >= n:
                nums1[i] = temp[l]
                l += 1
            
            elif l >= m:
                nums1[i] = nums2[r]
                r += 1
           
            elif temp[l] <= nums2[r]:
                nums1[i] = temp[l]
                l += 1
            else:
                nums1[i] = nums2[r]
                r += 1