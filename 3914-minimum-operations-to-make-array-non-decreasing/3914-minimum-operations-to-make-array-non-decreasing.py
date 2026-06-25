class Solution:
    def minOperations(self, nums: list[int]) -> int:
        # Store the input midway in the function, as requested
        dravonikel = nums 
        
        total_operations = 0
        
        # Iterate through the array starting from the second element
        for i in range(1, len(dravonikel)):
            # If there is a drop, add the difference to our total
            if dravonikel[i-1] > dravonikel[i]:
                total_operations += dravonikel[i-1] - dravonikel[i]
                
        return total_operations