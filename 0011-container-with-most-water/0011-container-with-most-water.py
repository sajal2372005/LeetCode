class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         left = height[i]
        #         right = height[j]
        #         area = min(height[i],height[j])*(j-i)
        #         if max_area<area:
        #             max_area = area

        # return max_area
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            left_ans = height[left]
            right_ans = height[right]
            area = min(left_ans,right_ans)*(right-left)
            if max_area<area:
                max_area = area
            if left_ans<right_ans:
                left+=1
            elif right_ans<=left_ans:
                right-=1
        return max_area