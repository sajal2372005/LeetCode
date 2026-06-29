class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            string = str(nums[i])
            final = 0
            for j in range(len(string)):
                if string[j] == '1':
                    final+=1
                elif string[j] == '2':
                    final+=2
                elif string[j] == '3':
                    final+=3
                elif string[j] == '4':
                    final+=4
                elif string[j] == '5':
                    final+=5
                elif string[j] == '6':
                    final+=6
                elif string[j] == '7':
                    final+=7
                elif string[j] == '8':
                    final+=8
                elif string[j] == '9':
                    final+=9
                elif string[j] == '0':
                    final+=0
            nums[i] = final
        nums.sort()
        return nums[0]