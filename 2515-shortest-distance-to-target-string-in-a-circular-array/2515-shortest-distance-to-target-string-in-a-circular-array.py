class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        val=0
        for i in range(0,len(words),1):
            if(words[i]==target):
                val = 1
                break
        
        if(val == 0):
            return -1

        right = right_traverse(words,target,startIndex)
        left = left_traverse(words,target,startIndex)
        if(right<left):
            return right
        if(left<right):
            return left
        if(left == right):
            return right

def right_traverse(words: List[str], target: str, startIndex: int) -> int:
    count = 0
    current = startIndex
    for i in range(0,len(words),1):
            
        if(words[current]!=target):
            current = ((current+1)%len(words))
            count = count +1
            
        else:
            break
    return count

def left_traverse(words: List[str], target: str, startIndex: int) -> int:
        count = 0
        current = startIndex
        for i in range(0,len(words),1):
            
            if(words[current]!=target):
                current = ((current-1+len(words))%len(words))
                count = count +1
            
            else:
                break
        return count        