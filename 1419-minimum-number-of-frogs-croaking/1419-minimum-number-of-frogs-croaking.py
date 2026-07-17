class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if croakOfFrogs[0] != 'c':
            return -1
        count_c = 0
        count_r = 0
        count_o = 0
        count_a = 0
        count_k = 0
        for i in range(len(croakOfFrogs)):
            if croakOfFrogs[i] == "c":
                count_c += 1
            elif croakOfFrogs[i] == "r":
                count_r += 1
            elif croakOfFrogs[i] == "o":
                count_o += 1
            elif croakOfFrogs[i] == "a":
                count_a += 1
            elif croakOfFrogs[i] == "k":
                count_k += 1
            if not(count_c >= count_r >= count_o >= count_a>= count_k):
                return -1
        if count_c == count_r == count_o == count_a == count_k:
            maxi = 0
            active = 0
            for i in range(len(croakOfFrogs)):
                if croakOfFrogs[i] == "c":
                    active += 1
                if croakOfFrogs[i] == "k":
                    active -= 1
                if maxi < active:
                    maxi = active
            return maxi
        else:
            return -1
