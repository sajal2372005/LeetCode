class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        left = 0
        right = len(chars) - 1
        
        while left < right:
            if not (ord(chars[left]) >= ord('a') and ord(chars[left]) <= ord('z') or ord(chars[left]) >= ord('A') and ord(chars[left]) <= ord('Z')) :
                left += 1
            elif not (ord(chars[right]) >= ord('a') and ord(chars[right]) <= ord('z') or ord(chars[right]) >= ord('A') and ord(chars[right]) <= ord('Z')):
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                
        return "".join(chars)