class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # count=0
        # for i in range(len(s)):
        #     sec = set()
        #     for j in range(i,len(s)):
        #         sec.add(s[j])
        #         if {'a','b','c'}<=sec:
        #             count+=1
        #             temp = len(s)-j-1
        #             count+=temp
        #             break
        # return count
        
        last_seen = {'a':-1,'b':-1,'c':-1}
        count = 0
        for i in range(len(s)):
            last_seen[s[i]] = i
            mini = min(last_seen['a'],last_seen['b'],last_seen['c'])
            count += (mini+1)
        return count