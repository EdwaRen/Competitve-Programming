class Solution:
    def islandPerimeter(self, grid):
        diameter = 0
        for row in range(len(grid)):
            for index in range(len(grid[0])):
                if grid[row][index] == 1:
                    shared = 0
                    if row+1 < len(grid) and grid[row+1][index] == 1: shared+=1
                    if row-1 >= 0 and grid[row-1][index] ==1: shared +=1
                    if index+1 < len(grid[0]) and grid[row][index+1] == 1: shared+=1
                    if index-1 >= 0 and grid[row][index-1] == 1: shared+=1
                    diameter += 4 - shared
        return diameter

a = Solution()
print(a.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
