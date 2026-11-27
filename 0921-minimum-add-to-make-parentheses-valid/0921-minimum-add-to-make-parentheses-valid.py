class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        remaining = []
        top =-1
        for i in range(len(s)):
            if s[i] == "(":
                top +=1
                stack.append("(")
            elif s[i] == ")":
                if top >-1 and stack[top] == "(":
                    stack.pop()
                    top -=1
                else:
                    remaining.append(")")
        if len(stack) > 0:
            return len(stack)+len(remaining)
        else:
            return len(remaining)