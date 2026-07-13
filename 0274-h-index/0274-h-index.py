class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sort = sorted(citations)
        sort = sort[::-1]
        count = 0
        for i in range(len(sort)):
            if sort[i] >= i+1:
                count+=1
            else: break
        return count