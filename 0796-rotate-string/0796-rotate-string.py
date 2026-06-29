class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        g = list(goal)
        for i in range(len(g)):
            if s!=g:
                temp = s.pop(0)
                s.append(temp)
            elif s == g:
                return True
        return False
        