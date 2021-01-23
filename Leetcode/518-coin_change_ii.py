class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int

        # DP algorithm with rows as coin denominationrs and cols as the amounts
        """
        
        dp = [1] + [0]*amount
        N = amount+1
        for c in coins:
            for i in range(c, N):
                if i - c >= 0:
                    dp[i] = dp[i] + dp[i-c]
        return dp[-1]

z = Solution()
amount = 10
coins = [10]
amount = 5
coins = [1, 2, 5]
print(z.change(amount, coins))
