class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        final = -1
        sets = set(nums1)
        nums2 = sorted(nums2)
        for i in range(len(nums2)):
            if nums2[i] in sets:
                final = nums2[i]
                break
        return final
            