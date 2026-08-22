class Solution:
    def checkDivisibility(self, n: int) -> bool:
        str_n = str(n)
        sum = 0
        product = 1
        for i in range(len(str_n)):
            sum += int(str_n[i])
            product *= int(str_n[i])
        total = sum + product
        if n % total == 0:
            return True
        else:
            return False