class Solution:
    def isValid(self, s: str) -> bool:
        lis = list(s)
        stack = []
        top = -1
        if lis[0] == "]" or lis[0] == ")" or lis[0] == "}":
            return False
        for i in range(len(lis)):
            if lis[i] == "(" :
                stack.append("(")
                top+=1
            elif lis[i] == "{" :
                stack.append("{")
                top+=1
            elif lis[i] == "[" :
                stack.append("[")
                top+=1
            
            if lis[i] == ")" :
                if top == -1:
                    return False
                if stack[top] == "(" :
                    stack.pop()
                    top-=1
                    continue
                else:
                    return False
            elif lis[i] == "}":
                if top == -1:
                    return False
                if stack[top] == "{":
                    stack.pop()
                    top-=1
                    continue
                else:
                    return False
            elif lis[i] == "]":
                if top == -1:
                    return False
                if stack[top] == "[":
                    stack.pop()
                    top-=1
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False
                
            
        