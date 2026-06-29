class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lis = sorted(stones)
        while len(lis) > 1:
            first = lis.pop(-1)
            second = lis.pop(-1)
            if first != second:
                result = first - second
                lis.append(result)
                lis = sorted(lis)
        return lis[0] if lis else 0
