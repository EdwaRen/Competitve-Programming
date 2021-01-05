class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """

        # Define N, handle inadequate jobs case
        N = len(jobDifficulty)
        if (d > N): return -1

        # Initialize dp list to be infinity for every value
        dp = [float('inf') for i in range(N)]
        dp.append(0)

        # Go through every day
        for i in range(1, d+1):
            # Find the minimum job difficulty starting at every index
            for j in range(0, N-i+1):
                maxJ = jobDifficulty[j]
                dp[j] = float('inf')

                # Check previous dp values to find the minimum job difficulty
                for k in range(j, N-i+1):
                    maxJ = max(maxJ, jobDifficulty[k])
                    dp[j] = min(dp[j], maxJ + dp[k+1])
                #print(j, dp[j])
            #print(i, dp)
        return dp[0]

z = Solution()
difficulties = [2, 1, 3, 1, 4, 1, 2, 1]
days = 4
print(z.minDifficulty(difficulties, days))

