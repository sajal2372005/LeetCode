import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # Edge case: If the array only has one element, it must be 1.
        if len(target) == 1:
            return target[0] == 1
        
        total_sum = sum(target)
        # Python's heapq is a min-heap, so we store negative values to simulate a max-heap
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)
        
        while max_heap[0] != -1:
            # Get the current maximum element (invert back to positive)
            current_max = -heapq.heappop(max_heap)
            
            # The sum of all other elements
            rest = total_sum - current_max
            
            # If rest is 1, we can always reach 1 by repeatedly subtracting 1 from current_max
            if rest == 1:
                return True
            
            # If rest is 0 (can't divide by 0) or the max element is smaller than the rest
            # (which means we can't work backwards anymore), it's impossible.
            if rest == 0 or current_max <= rest:
                return False
            
            # Calculate the previous value of the max element using modulo
            prev_val = current_max % rest
            
            # If prev_val is 0, it means the original element was 0, which is invalid (must be >= 1)
            if prev_val == 0:
                return False
            
            # Push the previous value back into the heap and update the total sum
            heapq.heappush(max_heap, -prev_val)
            total_sum = total_sum - current_max + prev_val
            
        return True