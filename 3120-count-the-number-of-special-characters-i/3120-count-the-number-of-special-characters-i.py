class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ord_lis = set()
        count = 0
        ans_lis = set()
        for char in word:
            ord_lis.add(ord(char))
        for char in word:
            if 'a'<=char<='z':
                if ((ord(char)-32) in ord_lis) and ((ord(char)-32)  not in ans_lis):
                    ans_lis.add(ord(char)-32)
                    count += 1
        return count
