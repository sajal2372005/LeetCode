class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # arr = [0]*k
        # binary = []
        # for i in range(2**k):
        #     temp = ""
        #     for x in arr:
        #         temp += str(x)
        #     if temp not in s:
        #         return False
        #     current = k-1
        #     if arr[current] == 0:
        #         arr[current] = 1
        #         continue
        #     if arr[current] == 1:
        #         while current and arr[current] != 0:
        #             arr[current] = 0
        #             current-=1
        #         if arr[current] ==0:
        #             arr[current] = 1
        # return True

        st = set()

        for i in range(len(s) - k + 1):
            st.add(s[i:i+k])

        return len(st) == 2**k