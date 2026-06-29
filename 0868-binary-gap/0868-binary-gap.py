class Solution:
    def binaryGap(self, n: int) -> int:
        maximum = 0
        left = -1
        right = -1
        
        bi = format(n,'b')
        for i in range(len(bi)):
            if bi[i] == "1":
                if left == -1:
                    left = i
                elif left>-1 and right == -1:
                    right = i

            
            if left > -1 and right > -1 and right>left:
                diff = 0
                diff = right -left
                if diff>maximum:
                    maximum = diff
                left = right
                right = -1
        return maximum