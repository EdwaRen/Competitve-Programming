import collections

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # Handle empty graph
        if not grid or len(grid) == 0:
            return -1

        M, N = len(grid), len(grid[0])
        
        # We use 2 matrixes to keep track of cumulative distances and unique building hits 
        distances, hits = [[0 for i in range(N)] for j in range(M)], [[0 for i in range(N)] for j in range(M)]
        
        # Keep track of total number of buildings for optimization
        buildings = sum([1 for row in grid for col in row if col == 1])
        
        def bfs(grid, row_orig, col_orig, distances, buildings):
            M, N = len(grid), len(grid[0])
            building_count = 0
            visited = [[False for i in range(N)] for j in range(M)]

            # BFs with a queue with row, col, and depth (distance)
            queue = collections.deque()
            queue.append((row_orig, col_orig, 0))

            while queue:
                row, col, depth = queue.popleft()

                # update distance and hits counter
                distances[row][col] += depth
                hits[row][col] += 1

                # Move all possible directions
                for direction in [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]:
                    if direction[0] >= M or direction[0] < 0 or direction[1] >= N or direction[1] < 0:
                        continue 
                    if visited[direction[0]][direction[1]]:
                        continue 

                    # Mark visited
                    visited[direction[0]][direction[1]] = True 

                    if grid[direction[0]][direction[1]] == 0:
                        queue.append((direction[0], direction[1], depth+1))
                    elif grid[direction[0]][direction[1]] == 1:
                        building_count += 1

            return building_count == buildings

        # BFS search on every building
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if not bfs(grid, row, col, distances, buildings):
                        return -1

        return min([distances[row][col] for row in range(M) for col in range(N) if grid[row][col] == 0 and hits[row][col] == buildings])

z = Solution()
grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(z.shortestDistance(grid))


            

        
