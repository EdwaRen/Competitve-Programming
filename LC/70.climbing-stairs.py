class Solution(object):
    def climbStairs(self, n):
        # Handle edge cases
        if n == 1:
            return 1
        if n <= 0:
            return 0

        # init dp array
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        # Iterate through to get all dp values
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        # return last value in array
        return dp[-1]

    def climbStairs_mem(self, n):
        # Init memo array, treated as 1-indexed
        memo = [0]*(n+1)

        # Recurse
        self.recurse(n, n, memo)
        return memo[-1]

    def recurse(self, index, n, memo):
        # Base cases
        if index == 0:
            return 1
        elif index < 0:
            return 0

        # Memoization
        if memo[index] > 0:
            return memo[index]

        # Set and return memo array
        memo[index] = self.recurse(index-1, n, memo) + self.recurse(index-2, n, memo)
        return memo[index]

        
a = Solution()
print(a.climbStairs(4))
