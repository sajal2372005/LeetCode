class Solution:
    def processStr(self, s: str) -> str:
        stack = []
        final_string = ""
        for i in range(len(s)):
            if s[i] == "*":
                if len(final_string)>0:
                    final_string = final_string[:-1]
                    
            elif s[i] == "#":
                if len(final_string)>0:
                    final_string += final_string
            elif s[i] == "%":
                final_string = final_string[::-1]
            else:
                final_string += s[i]
        return final_string

                
        