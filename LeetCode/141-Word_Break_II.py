class Solution(object):
    def wordBreak_old(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]

    def wordBreak(self, s, wordDict):
        if self.wordBreak_old(s, wordDict) == False:
            return []

        dp = [[] for i in range(len(s)+1)]
        def wordBreak_recurse( s, wordDict, start):
            if len(dp[start]) > 0:
                return dp[start]
            temp = []

            if start == len(s):
                temp.append("")

            for j in range(start+1, len(s)+1):
                if s[start:j] in wordDict:
                    suffix = wordBreak_recurse(s, wordDict, j)
                    for k in suffix:
                        space = " " if k != '' else ''
                        temp.append(s[start:j] +space + k)

            dp[start] = temp
            return temp

        return wordBreak_recurse(s, wordDict, 0)

a = Solution()
b = "catsanddog"
c = ["cat", "cats", "and", "sand", "dog"]
b = "pineapplepenapple"
c = ["apple", "pen", "applepen", "pine", "pineapple", 'posdpaod']
# b = 'aaaabaaaa'
# c = ['a', 'aa', 'aaaa']
print(a.wordBreak(b, c))

# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
