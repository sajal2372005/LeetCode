class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        string = ""
        for word in words:
            ans = 0
            for letter in word:
                temp = ord(letter)-97
                ans += weights[temp]
            ans = ans%26
            string+=(chr(ord("z")-ans))
        return string
