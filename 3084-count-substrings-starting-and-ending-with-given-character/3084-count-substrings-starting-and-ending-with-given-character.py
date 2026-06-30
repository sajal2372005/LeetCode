class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        # count = 0
        # for i in range(len(s)):
        #     if s[i] == c:
        #         count+=1
        # if count == 0:
        #     return 0
        # if count == 1:
        #     return 1
        # ans = count
        # for i in range(count-1,0,-1):
        #     ans+=i
        # return ans
        k = s.count(c)
        return k * (k + 1) // 2