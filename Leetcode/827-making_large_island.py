import collections

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        if N < 1: return 0
        M = len(grid[0])
        max_island_size = 0

        areas = collections.defaultdict(int)
        island = 1
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    island +=1
                    self.dfs(grid, i, j, areas, island, N, M)
                    max_island_size = max(max_island_size, areas[grid[i][j]])
          
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    max_local_size = 1
                    areas_seen = set()
                    if i+1 < N: 
                        max_local_size += areas[grid[i+1][j]]
                        areas_seen.add(grid[i+1][j])
                    if j+1 < M and grid[i][j+1] not in areas_seen: 
                        max_local_size += areas[grid[i][j+1]]
                        areas_seen.add(grid[i][j+1])

                    if j-1 >= 0 and grid[i][j-1] not in areas_seen:
                        max_local_size += areas[grid[i][j-1]]
                        areas_seen.add(grid[i][j-1])

                    if i-1 >= 0 and grid[i-1][j] not in areas_seen: 
                        max_local_size += areas[grid[i-1][j]]
                        areas_seen.add(grid[i-1][j])

                    max_island_size = max(max_island_size, max_local_size)
                    
        return max_island_size
                    
        
    def dfs(self, grid, i, j, areas, island, N, M):
        grid[i][j] = island
        areas[island] +=1
        
        for move in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if move[0] < 0 or move[0] >= N or move[1] < 0 or move[1] >= M:
                continue
            if grid[move[0]][move[1]] == 1:
                self.dfs(grid, move[0], move[1], areas, island, N, M)
                