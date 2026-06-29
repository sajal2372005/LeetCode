class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        op = 0
        while target > 1:
            if maxDoubles==0:
                return int(op+target-1)
            else:
                if target%2 != 0:
                    target = target-1
                    op +=1
                elif maxDoubles>0:
                    target = target/2
                    maxDoubles-=1
                    op+=1
                else: 
                    target = target-1
                    op+=1
        return op

        