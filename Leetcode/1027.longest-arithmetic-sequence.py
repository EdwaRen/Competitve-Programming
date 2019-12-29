import collections

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # dp[index][diff] => frequency
        dp = [collections.defaultdict(int) for i in range(len(A))]
        res = 0

        # Iterate over all possible index with existing differences
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                diff = A[i] - A[j]

                # Use existing sequence length or init sequence as length 2
                dp[j][diff] = max(dp[i][diff] + 1, 2)
                res = max(res, dp[j][diff])
        return res 

z = Solution()
A = [24,13,1,100,0,94,3,0,3]
A = [20,1,15,3,10,5,8]
A = [9,4,7,2,10]
A = [3,6,9,12]
print(z.longestArithSeqLength(A))

