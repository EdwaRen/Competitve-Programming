class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        Track the current indices visited, and at each step, if the characters
        match then we either increment one indice (t), or both (s and t).
        This creates two branches and is 2^N, however with dp or memoization
        it is reduced to O(NM).

        Normally a DP solution uses (i, j) to represent the
        indices visited in s and t. The number of combos is dp(i, j) =
        dp(i+1, j) + dp(i+1, j+1). Since we only rely on the next layer, we can
        consolidate this into a single dp dimension by going from the bottom up.
        """
        S, T = len(s), len(t)
        if S == 0 or T == 0 or T > S:
            return 0
        dp = [0 for i in range(S)]
        for i in range(S-1, -1, -1):
            prev = 1
            for j in range(T-1, -1, -1):
                old = dp[j]
                if s[i] == t[j]:
                    dp[j] += prev
                prev = old
        return dp[0]

z = Solution()
s = "babgbag"
t = "bag"
print(z.numDistinct(s, t))
