class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        data =  list(str(n))
        count = 0
        if(data[0]==str(x)):
            return False
        for i in range(1,len(data),1):
            if(data[i]==str(x)):
                count = 1
        if(count == 1):
            return True
        else:
            return False