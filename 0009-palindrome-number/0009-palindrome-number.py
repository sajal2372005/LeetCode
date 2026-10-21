class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        stri = str(x)
        output = True
        for i in range(len(stri)):
            if int(stri[i]) == int(stri[len(stri)-i-1]):
                continue
            else:
                output = False
        return output
        