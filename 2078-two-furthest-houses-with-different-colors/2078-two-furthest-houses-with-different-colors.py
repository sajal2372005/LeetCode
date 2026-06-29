class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        num = colors[0]
        val1=0
        val2=0
        current = len(colors)-1
        for i in range(len(colors)):
            
            if colors[current] == colors[i]:
                continue
            else:
                val1 = current-i
                break
        num = colors[0]
        current = len(colors)-1
        for i in range(len(colors)):
            
            if colors[current] == num:
                current-=1
                continue
            else:
                val2 = current-0
                break
        if val1>val2:
            return val1
        else:
            return val2

