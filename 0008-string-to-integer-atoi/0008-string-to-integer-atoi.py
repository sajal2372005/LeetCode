class Solution:
    def myAtoi(self, s: str) -> int:
        new_string = s.strip()
        lis = list(new_string)
        new_lis = []
        numbers = ['1','2','3','4','5','6','7','8','9','0','+']
        for num in range(len(lis)):
            if lis[num] == "+" and num!=0:
                break
            if lis[num] == "+" and num == 0:
                continue
            if num == 0 and lis[num] == '-':
                new_lis.append(lis[num])
                continue
            if lis[num] in numbers:
                new_lis.append(int(lis[num]))
            if lis[num] not in numbers:
                break
        if not new_lis:
            return 0
        result = 0
        if new_lis[0] == "-":
            new_lis.remove("-")
            for digit in new_lis:
                result = result * 10 + digit
            if result>2**31:
                result = 2**31
            new_result = 0-result
            return new_result    
        
        for digit in new_lis:
            result = result * 10 + digit
        if result>2**31 - 1:
            result = 2**31 - 1
        return result
        