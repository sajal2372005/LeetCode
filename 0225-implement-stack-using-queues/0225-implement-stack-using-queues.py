class MyStack:

    def __init__(self):
        self.list = []
        

    def push(self, x: int) -> None:
        self.list.append(x)
        

    def pop(self) -> int:
        return self.list.pop()
        

    def top(self) -> int:
        temp = self.list.pop()
        self.list.append(temp)
        return temp
        

    def empty(self) -> bool:
        if self.list:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()