class Solution:
    def checkString(self, s: str) -> bool:
        str = "a"
        count = 1
        for i in range(len(s)):
            if s[i] == str:
                continue
            elif s[i] == "b" and count == 1:
                str = "b"
                count = 0
                continue
            else:
                return False
        return True

        