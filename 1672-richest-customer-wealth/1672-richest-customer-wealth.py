class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for arr in accounts:
            temp = 0
            for num in arr:
                temp += num
            if temp > max:
                max = temp
            
        return max
