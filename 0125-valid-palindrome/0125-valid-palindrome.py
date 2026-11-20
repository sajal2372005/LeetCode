class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        final = ""
        for i in range(len(string)):
            if ord(string[i]) >= ord('a') and ord(string[i]) <= ord('z') or ord(string[i]) >= ord('0') and ord(string[i]) <= ord('9'):
                final += string[i]
        if len(string) <= 1:
            return True
        left = 0
        Right = len(final)-1
        for i in range(len(final)):
            if final[Right] != final[left]:
                return False
            else:
                Right -=1
                left +=1
        return True

         