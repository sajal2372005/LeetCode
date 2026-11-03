from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        half = ''.join(c * (cnt[c] // 2) for c in sorted(cnt))
        mid = ''.join(c for c in cnt if cnt[c] % 2)
        return half + mid + half[::-1]