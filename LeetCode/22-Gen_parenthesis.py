class Solution:
    def generateParenthesis(self, input):
        ans  = []
        def backtrack(M, l, r):
            if len(M) == 2*input:
                ans.append(M)
                return
            if l < input:
                backtrack(M+'(', l+1, r)
            if l > r:
                backtrack(M+')', l, r+1)
        backtrack('', 0, 0)
        print("answer", ans)

a = Solution()
a.generateParenthesis(1)
