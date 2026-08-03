class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word += 'a'
        count= 0
        sets = set()
        turn = "letter"
        temp = ""
        for i in range(len(word)):
            if ord(word[i]) >47 and ord(word[i])<58:
                turn = "number"
            else:
                turn = "letter"
            if turn == "letter":
                if temp != "":
                    num = int(temp)
                    if num not in sets:
                        sets.add(num)
                        count+=1
                    temp = ""
                continue
            elif turn == "number":
                temp += word[i]
        return count