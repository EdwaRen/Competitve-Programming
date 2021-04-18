class Solution:
    def letterCombinations(self, digits):
        if not digits: return ''

        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        self.dfs(digits, res, '', mapping)
        return res

    def dfs(self, digits, res, cur, mapping):
        if not digits:
            res.append(cur)
            return 
        for c in mapping[int(digits[0])]:
            self.dfs(digits[1:], res, cur + c, mapping)

z = Solution()
digits = ""
print(z.letterCombinations(digits))
