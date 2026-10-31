class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        top = -1
        bottom = 0
        final = ""
        for i in range(len(s)):
            if s[i] == "(" and top == -1:
                stack.append("(")
                top+=1
            elif s[i] == "(" and top != -1:
                stack.append("(")
                top+=1
                final+="("
            elif s[i] == ")" and i == 0:
                return 0
            
            if s[i] == ")" and top != 0:
                final+=")"
                stack.pop()
                top-=1
            elif s[i] == ")" and top == 0:
                stack.pop()
                top-=1
        return final
