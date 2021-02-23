class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        Memoization to cache result. The cache has the number of elements larger
        than the current that can be reached. No need for a cache to ever be updated
        """
        res = 0
        M = len(matrix)
        N = len(matrix[0])
        memo = [[0 for i in range(N)] for j in range(M)]

        for i in range(M):
            for j in range(N):
                res = max(res, self.dfs(i, j, matrix, memo))

        return res 

    def dfs(self, x, y, matrix, memo):
        if memo[x][y] != 0: return memo[x][y]
        M = len(matrix)
        N = len(matrix[0])

        for dir in [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]:
            if dir[0] >= 0 and dir[0] < M and dir[1] >= 0 and dir[1] < N and matrix[dir[0]][dir[1]] > matrix[x][y]:
                memo[x][y] = max(memo[x][y], self.dfs(dir[0], dir[1], matrix, memo))
        
        memo[x][y] += 1
        return memo[x][y]

z = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(z.longestIncreasingPath(matrix))