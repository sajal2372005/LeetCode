class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        arr = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                temp = s[i:j]
                arr.append(temp)
        maxi = 0
        
        for i in (arr):
            dic = {}
            flag = 0
            for j in range(len(i)):
                if i[j] not in dic:
                    dic[i[j]] = 1
                else:   
                    dic[i[j]]+=1
            for j in (dic):
                if dic[j] > 2:
                    flag = 1
            if flag:
                continue
            else:
                maxi = max(maxi,len(i))
        return maxi
                    
                
