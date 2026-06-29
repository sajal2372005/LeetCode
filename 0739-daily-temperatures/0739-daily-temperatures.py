class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # This will store indices of days waiting for a warmer temp
        
        for i, current_temp in enumerate(temperatures):
            # While stack is not empty AND today is warmer than the day at the top of the stack
            while stack and current_temp > temperatures[stack[-1]]:
                popped_index = stack.pop()
                # The wait time is the difference between today's index and the past day's index
                ans[popped_index] = i - popped_index
            
            # Add today's index to the stack to wait for a warmer day
            stack.append(i)
            
        return ans