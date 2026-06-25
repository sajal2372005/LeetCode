class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}
        if len(s)!=len(t):
            return False

        s_lis = list(s)
        t_lis = list(t)
        for i in range(len(s_lis)):
            if s_lis[i] not in s_dic:
                s_dic[s_lis[i]] = 0
            s_dic[s_lis[i]] += 1

            if t_lis[i] not in t_dic:
                t_dic[t_lis[i]] = 0
            t_dic[t_lis[i]] += 1
        
        
        return s_dic == t_dic
        
