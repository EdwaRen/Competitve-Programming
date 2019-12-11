class Solution:
    def findTargetSumWays(self, nums, S):

        # Calculate the positive sum
        p_sum = sum(nums) - S
        
        # Handle edge cases. Question guarantees sum < 1000
        if p_sum % 2 == 1 or S > 1000:
            return 0
        elif p_sum < 2:
            p_sum = sum(nums) + S

        # Get positive sum knowing there will be no remainder
        p_sum = int(p_sum/2)

        # Init dp array. The DP holds the possibilities to achieve a certain sum
        dp = [0] * (p_sum+1)
        dp[0] = 1
        
        # Iterate through all nums
        for i in nums:
        
            # Iterate through all possible sums
            for j in reversed(range(p_sum+1)):
                if j - i >= 0:
                    dp[j] += dp[j-i]
        return dp[p_sum]


z = Solution()
nums = [1]
s = 1
print(z.findTargetSumWays(nums, s))







