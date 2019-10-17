class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        dp = [[[float('-inf') for i in range(N+1)] for j in range(N+1)] for k in range(N+1)]
        dp[1][1][1] = 0

        for x1 in range(1, N+1):
            for y1 in range(1, N+1):
                for x2 in range(1, N+1):
                    y2 = x1 + y2 - x2 
                    if (y2 < 0 or y2 > N or y1 < 1 or grid[x1][y1] == -1 or grid[x2][y2] == -1):
                        continue

                    cur = max(dp[x1-1][y1][x2-1], dp[x1-1][y1][x2], dp[x1][y1-1][x2], dp[x1][y1-1][x2-1])
                    if cur < 0:
                        continue 
                    
                    cur += grid[x1][y1]
                    if x1 != x2:
                        cur += grid[x2][y2]

                    dp[x1][y1][x2] = cur

        
z = Solution()
grid = [
    [0, 1, -1],
    [1, 0, -1],
    [1, 1,  1]
]
print(z.cherryPickup(grid))