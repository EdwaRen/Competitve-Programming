class Solution:
    def letterCombinations(self, digits):
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        comb = ['']
        for num in digits:
            tempcomb = ['']
            for letter in mapping[int(num)]:
                for index in range(len(comb)):
                    tempcomb.append(comb[index] + letter)
            comb = tempcomb[:]
            comb.pop(0)
        if comb[0] == '':
            comb.pop(0)
        return comb

a = Solution()
print(a.letterCombinations(""))
