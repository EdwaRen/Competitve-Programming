class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Map cell to max island size and starting cell from that cell
        Go through all cells and find the sum of all adjacent cells
            if they have a different start.
        detailed_grid[i][j] = { start: max }
        """
        N = len(grid)
        M = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:


    def fill_cells(self, N, M, grid, index, row, col):
        res = 0
        grid[row][col] = index
        for move in self.moves(row, col):
            i, j, = move 
            if i >= N or i < 0 or j >= N or j < 0:
                continue
            if grid[i][j] == 1:
                res += self.fill_cells(N, M, grid, index, i, j) + 1
        return res


    def moves(self, row, col):
        return [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]


        