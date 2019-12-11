class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Key Insights to solve this problem
        * Path A and path B are equivalent to both going from (0, 0) to (n-1, n-1)
        * (x1, y1), (x2, y2) are coordinates for path A and path B
        * If Path A and Path B both want the same cherry at (x, y), they MUST be on the same step
            * Ie they must both be on their 3rd move even if they got there independently.

        * dp[x1][y1][x2] represents the max cherries picked at step (x1+y1) = (x2 + y2)
        * Similarly, y2 = (x1+y1 - x2)
        * At dp[x1][y1][x2] there are 4 possible places to have picked their cherries
            * up-up, up-left, left-up, left-left
            * Permutations of A and B going either up or left
        * Memoize and dp!
        """
        N = len(grid)
        dp = [[[float('-inf') for i in range(N+1)] for j in range(N+1)] for k in range(N+1)]
        dp[1][1][1] = grid[0][0]

        for x1 in range(1, N+1):
            for y1 in range(1, N+1):
                for x2 in range(1, N+1):
                    y2 = x1 + y1 - x2 
                    if (dp[x1][y1][x2] > 0 or y2 < 0 or y2 > N or y1 < 1 or grid[x1-1][y1-1] == -1 or grid[x2-1][y2-1] == -1):
                        continue

                    cur = max(dp[x1-1][y1][x2-1], dp[x1-1][y1][x2], dp[x1][y1-1][x2], dp[x1][y1-1][x2-1])
                    if cur < 0:
                        continue 

                    cur += grid[x1-1][y1-1]
                    if x1 != x2:
                        cur += grid[x2-1][y2-1]

                    dp[x1][y1][x2] = cur
        if dp[N][N][N] == float('-inf'):
            return 0
        return dp[N][N][N]

        
z = Solution()
grid = [
    [0, 1, -1],
    [1, 0, -1],
    [1, 1,  1]
]
grid = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1]
]
grid = [
    [1,1,-1],
    [1,-1,1],
    [-1,1,1]
]

print(z.cherryPickup(grid))