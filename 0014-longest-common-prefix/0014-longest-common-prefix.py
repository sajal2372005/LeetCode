class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = len(strs[0])
        for i in range(len(strs)):
            if small > len(strs[i]):
                small = len(strs[i])
        output = ""
        for i in range(small):
            commen = ""
            count = len(strs)
            for j in range(len(strs)):
                if commen == "":
                    commen = strs[j][i]
                    count -=1
                else:
                    if commen == strs[j][i]:
                        count-=1
                        continue
            if count == 0:
                output += commen
            else :
                break
        return output

