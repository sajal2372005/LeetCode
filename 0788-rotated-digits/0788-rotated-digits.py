class Solution:
    def rotatedDigits(self, n: int) -> int:
        def rotate(num: int)-> str:
            str_num = str(num)
            str_output = ''
            for i in range(len(str_num)):
                if str_num[i] == "0" or str_num[i] == '1' or str_num[i] == '8':
                    str_output += str_num[i]
                elif str_num[i] == '2':
                    str_output += '5'
                elif str_num[i] == '5':
                    str_output += '2'
                elif str_num[i] == '9':
                    str_output += '6'
                elif str_num[i] == '6':
                    str_output += '9'
                else:
                    str_output += 'a'
            return str_output



        count = 0
        for i in range(n+1):
            temp = rotate(i)
            if 'a' in temp:
                continue
            else:
                temp = int(temp)
                if temp == i:
                    continue
                else:
                    count+=1
        return count
