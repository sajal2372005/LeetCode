class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = list(ransomNote)
        m = list(magazine)
        r_dic = {}
        m_dic = {}
        for i in range(len(r)):
            if r[i] not in r_dic:
                r_dic[r[i]] = 0
            r_dic[r[i]] += 1
        for i in range(len(m)):
            if m[i] not in m_dic:
                m_dic[m[i]] = 0
            m_dic[m[i]] += 1

        for num in r_dic:
            count = r_dic[num]
            if num not in m_dic:
                return False
            if m_dic[num]<count:
                return False
        return True
        

        