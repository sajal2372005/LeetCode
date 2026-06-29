class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            count = prices[i]
            for j in range(i+1,len(prices),1):
                if prices[j]<=prices[i]:
                    count = prices[i] - prices[j]
                    break
            ans.append(count)
        return ans

        