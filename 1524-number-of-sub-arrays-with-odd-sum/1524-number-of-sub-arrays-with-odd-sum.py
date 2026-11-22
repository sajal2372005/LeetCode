class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # subarr = []
        # sumarr = []
        # for i in range(len(arr)):
            
        #     for j in range(i,len(arr)):
        #         sub = []
        #         for k in range(i,j+1):
        #             sub.append(arr[k])
        #         subarr.append(sub)
        # for a in subarr:
        #     final_num = 0
        #     for num in a:
        #         final_num+=num
        #     sumarr.append(final_num)
        # count = 0
        # for i in sumarr:
        #     if i%2 != 0:
        #         count+=1
        # return count % (10**9 + 7)

        evencount = 1
        oddcount = 0
        result = 0
        prefix = 0
        for i in range(len(arr)):
            prefix += arr[i]
            if prefix % 2 == 0:
                result += oddcount
                evencount+=1
            else:
                result += evencount
                oddcount+=1
        return result % (10**9+7)