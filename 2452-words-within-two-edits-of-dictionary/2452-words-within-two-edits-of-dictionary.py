class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q_word in queries:
            for d_word in dictionary:

                diff = 0
                for q_char,d_char in zip(q_word,d_word):
                    if q_char != d_char:
                        diff+=1
                if diff<=2:
                    ans.append(q_word)
                    break
        return ans