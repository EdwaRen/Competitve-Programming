class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        # Init first dp list
        dp = [0 for i in range(target)]
        for i in range(min(f, target)):
            dp[i] = 1

        # Each following count can be calculated from the (d-2) dice frequencies
        for i in range(1, d):

            # Keep track of the current sum and able to reference old values to delete
            cur_sum = 0
            next_dp = list(dp)
            
            # Set initial zeroes
            for j in range(i):
                if j - f >= 0:
                    cur_sum -= next_dp[j-f]
                cur_sum += next_dp[j]
                next_dp[j] = 0

           # Generate the possiblities for the next dice
            for j in range(i, target):
                tmp = next_dp[j]
                next_dp[j] = cur_sum

                 # We can only count back f times since we only have f faces.
                if j - f >= 0:
                    cur_sum -= dp[j-f]
                cur_sum += tmp
                
            dp = next_dp

        return dp[-1] % ((10**9)+7)


z = Solution()
d = 20
f = 19
target = 233
print(z.numRollsToTarget(d, f, target))
        
