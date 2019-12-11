class Solution(object):
    def countBits(self, num):
        cur = 2

        # number of ones per num value
        dp = [0] * (num+1)
        i = 1

        # Ensure it doesn't end early, so we multiple num by two
        while cur <= num*2:
            
            # Takes the last 2^n values and just adds one more to their value            
            while i < cur and i <= num:
                dp[i] = dp[i - (cur>>1)] + 1
                i+=1
    
            # Multiple by two
            cur = cur << 1


        return dp

z = Solution()
num = 16
print(z.countBits(num))





