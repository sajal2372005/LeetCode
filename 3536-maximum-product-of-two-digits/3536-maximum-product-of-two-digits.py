class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        maxi = 0
        for i in range(len(s)):
            first = int(s[i])
            for j in range(i+1,len(s)):
                if i == j:
                    continue
                sec = int(s[j])
                multi = first * sec
                if maxi < multi:
                    maxi = multi
        return maxi

