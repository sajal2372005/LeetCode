class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a':-1,'b':-1,'c':-1}
        count = 0
        for i in range(len(s)):
            last_seen[s[i]] = i
            mini = min(last_seen['a'],last_seen['b'],last_seen['c'])
            count += (mini+1)
        return count