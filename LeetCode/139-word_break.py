class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[0] = True
        # print("s leng", len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                # print("check", i, j, s[i:j+1], dp[i], dp)
                if dp[i] and s[i:j+1] in wordDict:
                    # print("True set", dp, i, j)
                    dp[j+1] = True
        return dp[-1]

        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
a = Solution()
print(a.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
