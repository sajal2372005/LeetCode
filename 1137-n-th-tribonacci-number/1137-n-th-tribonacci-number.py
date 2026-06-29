class Solution:
    def tribonacci(self, n: int) -> int:
        trip = 0
        first = 0
        second = 1
        third = 1
        final = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 2
        for i in range(n):
            if i == 1 or i==0 or i==2:
                continue
            if trip == 0:
                first = first+second+third
                final = first+second+third
                trip =1
            elif trip == 1:
                second = first+second+third
                final = first+second+third
                trip = 2
            elif trip == 2:
                third = first+second+third
                final = first+second+third
                trip = 0

        return final