class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set2 = set()
        ans = []
        for i in range(len(A)):
            set2.add(B[i])
            count = 0
            for j in range(i+1):
                if A[j] in set2:
                    count+=1
            ans.append(count)
        return ans
        

        