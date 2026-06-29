class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            num = nums[i]
            binary = format(num,'b')
            rev = binary[::-1]
            if rev[0] == 1:
                rev = '0'+rev
            ind = int(rev,2)
            ans.append((ind,num))
        ans.sort()
        final = []
        for i in ans:
            final.append(i[1])
        return final
            