class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Edge case: if the list is completely empty
        if not strs:
            return ""

        max_len = 200
        for i in range(len(strs)):
            # CORRECTED: Use strs[i] to check the length of each string
            if len(strs[i]) < max_len:
                max_len = len(strs[i])
                
        final_str = ""
        
        for i in range(max_len):
            common = strs[0][i]
            count = 0
            for j in range(len(strs)):
                char = strs[j]
                if char[i] == common:
                    count += 1
                    continue
                else:
                    break
                    
            if count == len(strs):
                final_str += common
            else:
                break
                
        return final_str