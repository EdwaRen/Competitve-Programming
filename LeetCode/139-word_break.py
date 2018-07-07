class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]
a = Solution()
print(a.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
