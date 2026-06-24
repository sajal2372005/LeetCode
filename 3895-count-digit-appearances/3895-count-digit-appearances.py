class Solution(object):
    def countDigitOccurrences(self,nums, target_digit):
        count = 0;
        target_str = str(target_digit)

        for number in nums:
            for char in str(number):
                if char == target_str:
                    count +=1
        return count
                
        