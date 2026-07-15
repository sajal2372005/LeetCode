class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_arr = []
        right_arr = []
        for i in range(len(nums)):
            noti = ~i
            total = 0
            rev_total = 0
            for j in range(i+1,len(nums)):
                total += nums[j]
            right_arr.append(total)
            for j in range(0,i):
                rev_total += nums[j]
            left_arr.append(rev_total)
        answer = []
        for i in range(len(nums)):
            ans = abs(right_arr[i] - left_arr[i])
            answer.append(ans)
        return answer
        