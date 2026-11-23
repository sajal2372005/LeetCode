class ProductOfNumbers:

    # def __init__(self):
    #     self.arr = []
        

    # def add(self, num: int) -> None:
    #     self.arr.append(num)
        

    # def getProduct(self, k: int) -> int:
    #     final = 1
    #     k = k
    #     indx = len(self.arr)-1
    #     while k:
    #         final *= self.arr[indx]
    #         indx -=1
    #         k -=1
    #     return final
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)