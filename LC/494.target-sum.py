class Solution:
    def findTargetSumWays(self, nums, S):
        p_sum = sum(nums) + s     
        if p_sum & 1:
            return 0
        p_sum = p_sum >> 1

        dp = [0] * (sum(nums) + 1)
        
        for i in range(1, len(nums)):
            local_sum = 0
            for j in reverse(i):
                local_sum +=j
                dp[local_sum] +=1 
                







