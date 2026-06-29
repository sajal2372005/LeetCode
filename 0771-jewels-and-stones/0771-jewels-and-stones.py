class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set()
        count=0
        for j in jewels:
            jewel.add(ord(j))
        stone = list(stones)
        for i in range(len(stone)):
            if ord(stone[i]) in jewel:
                count+=1
        return count