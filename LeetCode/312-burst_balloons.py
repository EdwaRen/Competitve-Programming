# class Solution(object):
#     def maxCoins(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums = [1] + nums + [1]
#         n = len(nums)
#         dp = [[0] * n for _ in xrange(n)]
#
#         def calculate(i, j):
#             if dp[i][j] or j == i + 1: # in memory or gap < 2
#                 return dp[i][j]
#             coins = 0
#             for k in xrange(i+1, j): # find the last balloon
#                 coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
#             dp[i][j] = coins
#             return coins
#
#         return calculate(0, n-1)



class Solution(object):


    def maxCoins(self, nums):
        # Safe nums
        s_nums = [1] + nums + [1]
        print(s_nums)
        n = len(s_nums)
        memo = [[0 for j in range(n)] for i in range(n) ]

        def recurse(s, e):
            if s + 1 == e:
                return memo[s][e]
            if memo[s][e] > 0:
                return memo[s][e]
            coins = 0
            for i in range(s+1, e):
                coins = max(coins, s_nums[s]* s_nums[i]*s_nums[e] + recurse(s, i) + recurse(i, e)  )
            memo[s][e] = coins
            print(s, e, coins, memo)
            return coins

        return recurse(0, n-1)
a = Solution()
b = [3, 1, 5, 8]
print(a.maxCoins(b))
