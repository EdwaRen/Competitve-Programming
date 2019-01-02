class Solution(object):
    def coinChangeIter(self, coins, amount):
        sum = 0
        dp = [0 for i in range(amount+1)]

        for i in range(1, amount+1):
            min = -1
            for coin in coins:
                if i-coin >= 0 and dp[i-coin] != -1:
                    if min < 0 or dp[i-coin] +1 < min:
                        min = dp[i-coin] + 1

            dp[i] = min
        return dp[amount]

    def coinChange(self, coins, amount):
        dp = [0 for i in range(amount+1)]
        a = self.coinChangeRecurse(coins, amount, dp)
        return a

    def coinChangeRecurse(self, coins, rem, dp):
        if rem == 0:
            return 0
        if rem < 0:
            return -1
        if dp[rem] != 0:
            return dp[rem]

        min = 9999999
        for coin in coins:
            a = self.coinChangeRecurse(coins, rem-coin, dp)
            if a >= 0 and a < min:
                min = a +1

        if min == 9999999:
            min = -1

        dp[rem] = min
        return min

a = Solution()
print(a.coinChange([1, 2, 5], 11))
print(a.coinChange([2], 3))
