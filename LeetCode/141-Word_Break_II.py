class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [[] for i in range(len(s)+1)]
        # print(dp, len(s))
        dp[0] = ['']
        for i in range(len(s)+1):
            # print("i iterate", dp)
            temp = []

            for j in range(i, len(s)+1):
                if s[i:j] in wordDict and len(dp[i])>=1:

                    if dp[i] != ['']:
                        for k in dp[i]:
                            # print("adding k", k, dp[i])
                            temp.append( k + " " +  s[i:j] )
                    else:
                        temp.append( s[i:j])
                    print("adding", i, j, s[i:j], dp[j], dp)
            dp[i] = temp
        print("dp final", dp)
        return dp[len(s)]
a = Solution()
b = "catsanddog"
c = ["cat", "cats", "and", "sand", "dog"]
b = "pineapplepenapple"
c = ["apple", "pen", "applepen", "pine", "pineapple"]
print(a.wordBreak(b, c))

# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
