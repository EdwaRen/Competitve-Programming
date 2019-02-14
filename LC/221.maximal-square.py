class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        dp = [[0]*len(matrix[0]) for i in range(len(matrix))]
        square_max = 0
        print(dp)

        dp[0] = matrix[0]
        for i in range(len(matrix)):
            dp[i][0] = matrix[i][0]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
                if dp[i][j] > square_max:
                    square_max = dp[i][j]
                            
        return square_max*square_max


#        """
#        :type matrix: List[List[str]]
#        :rtype: int
#        """

z = Solution()
matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
print(z.maximalSquare(matrix))
