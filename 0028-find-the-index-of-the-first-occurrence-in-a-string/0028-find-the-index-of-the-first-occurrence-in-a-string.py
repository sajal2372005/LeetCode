class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        num = 0
        lis = list(haystack)
        need = list(needle)
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                if lis[i] == need[0]:
                    current = i
                    string = str()
                    count = 0
                    while current < len(lis) and count < len(need) and lis[current] == need[count]:
                        string += lis[current]
                        current +=1
                        count+=1
                    if string == needle:
                        return i
                else:
                    continue