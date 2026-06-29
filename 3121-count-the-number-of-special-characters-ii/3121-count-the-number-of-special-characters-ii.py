class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lis_set = set()
        banned = set()
        for w in word:
            lis_set.add(ord(w))
        lis = list(word)
        stack = set()
        for i in range(len(lis)):
            if ord(lis[i])>=65 and ord(lis[i])<=90:
                if (ord(lis[i])+32) not in lis_set:
                    continue
                elif (ord(lis[i])) not in banned:
                    stack.add(ord(lis[i]))
            if ord(lis[i])>=97 and ord(lis[i])<=122:
                if (ord(lis[i])-32) not in lis_set:
                    continue
                elif ord(lis[i])-32 not in stack:
                    continue
                elif ord(lis[i])-32 in stack:
                    stack.remove(ord(lis[i])-32)
                    banned.add(ord(lis[i])-32)
                    if ord(lis[i])-32 in stack:
                        stack.remove(ord(lis[i])-32)
        return len(stack)
        