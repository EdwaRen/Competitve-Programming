class Solution:
    def numTrees(self, n):
        factorial1 = 1
        factorial2 = 1
        for i in range(2*n):
            factorial1 *= (i+1)

        for i in range(n):
            factorial2 *= (i+1)
        
        return int(factorial1 / (factorial2 * factorial2 * (n+1)))

    def numTreesProper(self, n):
        """
        Uses the property that the number of possible subtrees at root i is left tree * right tree
        This is for all i in n, thus O(n^2)
        """
        # Handle edge case
        if n < 2:
            return n

        # Init
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
    
        # Loop through all n
        for i in range(2, n+1):
            for j in range(1, i+1):
                # Inner loop finds number of BSTs possible with i possible nodes
                dp[i] += dp[j-1]*dp[i-j]

        # Possibilties at n is just last element of dp
        return dp[-1]        


z = Solution()
num = 7
print(z.numTrees(7))









