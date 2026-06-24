class Solution:
    def mirrorDistance(self, n: int) -> int:
        data = reverse(n)
        num = abs(n-data)
        return num


def reverse(num:int):
    data = int(str(num)[::-1])
    return data
        