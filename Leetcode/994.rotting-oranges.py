import collections

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # Catch edge case
        if not grid or len(grid) == 0: return -1

        # General idea is to BFS from every infected orange using a queue
        M, N = len(grid), len(grid[0])
        queue = collections.deque()

        # Keep track of total oranges to check if all oranges have been infected at the end
        oranges_total = 0
        oranges_infected = 0

        # Find all infected oranges and add to queue to bfs in next step
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    oranges_infected += 1
                if grid[row][col] == 1 or grid[row][col] == 2:
                    oranges_total += 1
        
        # BFS while keeping track of the maximum valid distance reached
        max_dist = 0
        while queue:
            row, col, dist = queue.popleft()

            # Go through all possible moves
            for move in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if move[0] < 0 or move[0] >= M or move[1] < 0 or move[1] >= N:
                    continue 

                # Valid, untouched orange to be infected
                if grid[move[0]][move[1]] == 1:
                    queue.append((move[0], move[1], dist+1))
                    grid[move[0]][move[1]] = 2
                    max_dist = max(max_dist, dist+1)
                    oranges_infected+=1
                
        return max_dist if oranges_infected == oranges_total else -1
        
z = Solution()
grid = [[2,1,1],[0,1,1],[1,0,1]]
# grid = [[2,1,1],[1,1,0],[0,1,1]]
print(z.orangesRotting(grid))