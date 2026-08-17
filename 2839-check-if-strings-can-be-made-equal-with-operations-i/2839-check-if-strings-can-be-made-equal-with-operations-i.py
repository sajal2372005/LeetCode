class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        result = True
        for i in s2:
            if i not in s1:
                return False
        if s1[0]!=s2[0]:
            if s1[0] != s2[2]:
                result = False
        if s1[1] !=s2[1]:
            if s1[1] != s2[3]:
                result = False
        if s1[2] !=s2[2]:
            if s1[2] != s2[0]:
                result = False
        if s1[3] !=s2[3]:
            if s1[3] != s2[1]:
                result = False
        return result

        