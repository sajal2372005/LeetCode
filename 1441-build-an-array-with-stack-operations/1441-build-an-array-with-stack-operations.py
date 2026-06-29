class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        lis = set(target)
        top = -1
        output = []
        for i in range(n+1):
            if i == 0:
                continue
            top+=1
            stack.append(i)
            top+=1
            output.append("Push")
            if i not in lis:
                output.append("Pop")
                stack.remove(i)
            if stack == target:
                return output
            
