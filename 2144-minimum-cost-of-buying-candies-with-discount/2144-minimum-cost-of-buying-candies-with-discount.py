class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        sort_lis = sorted(cost)
        rev = sort_lis[::-1]
        count = 0
        ans = 0
        for i in range(len(rev)):
            if count == 2:
                count = 0
                continue
            else:
                ans += rev[i]
                count+=1

        return ans                