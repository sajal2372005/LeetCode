import sys
sys.set_int_max_str_digits(1000000) # Increase limit to 10,000 digits
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        string  = "".join(map(str,num))
        integer = int(string)
        total = integer+k
        lis = []
        for digit in str(total):
            lis.append(int(digit))
        return lis
