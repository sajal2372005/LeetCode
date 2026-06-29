class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        string = str()
        know_set = {key:value for key,value in knowledge}
        turn = 0
        for  i in range(len(s)):
            if turn == 1:
                if s[i] == ')':
                    turn = 0
                continue
            if s[i] == '(':
                turn = 1
                current = i+1
                temp = str()
                while s[current] != ')':
                    temp = temp+s[current]
                    current+=1
                if temp in know_set:
                    string = string+know_set[temp]
                elif temp not in know_set:
                    string = string+'?'
            else:
                string = string+s[i]
        return string