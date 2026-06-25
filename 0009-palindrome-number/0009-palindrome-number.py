class Solution:
    def isPalindrome(self, x: int) -> bool:
        stri = str(x)
        return stri == stri[::-1]