from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = float('inf')  # Start with an infinitely large distance
        
        for i in range(len(nums)):
            if nums[i] == target:
                # Calculate absolute distance using Python's built-in abs()
                distance = abs(i - start) 
                
                # If this is the closest one we've seen, update our record
                if distance < min_distance:
                    min_distance = distance
                    
        return min_distance