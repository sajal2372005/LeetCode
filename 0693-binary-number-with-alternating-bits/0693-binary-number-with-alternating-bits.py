class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = f"{n:b}"
        # num = binary[0]
        # for i in range(1,len(binary)):
        #     if num == "0":
        #         if binary[i] == "0":
        #             return False
        #         else:
        #             num = binary[i]
        #     elif num == '1':
        #         if binary[i] == '1':
        #             return False
        #         else:
        #             num = binary[i]

        # return True

        if "00" in binary or "11" in binary:
            return False
        else:
            return True
