class Solution(object):
    def minDistance(self, s, p):
        # dp keeps track of how many turns it takes for each substring to get to another substring
        dp = [[999999 for x in range(len(p)+1)] for y in range(len(s)+1)]         
        
        # Set initial values
        for i in range(len(s)+1):
            dp[i][0] = i
        for j in range(len(p)+1):
            dp[0][j] = j

        # Go through every permutatino of substrings to find shortest path
        for i in range(len(s)):
            for j in range(len(p)):
                                    
                # We can reduce steps taken by 1 if the current character is the same in both strings
                if s[i] == p[j]:
                    dp[i+1][j+1] = min(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j])
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) +1
        
        return dp[-1][-1]

z = Solution()
s1 = "intention"
s2 = "execution"
print(z.minDistance(s1, s2))
