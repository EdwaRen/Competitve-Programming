class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        Breadth first search using two matrices to keep track of which cells
        are reachable from both sets of borders
        """
        pacific_filled = [[False for i in matrix[0]] for j in matrix]
        atlantic_filled = [[False for i in matrix[0]] for j in matrix]

        res = []

        for i in range(len(matrix[0])):
            self.bfs(0, i, matrix, pacific_filled, 1)
        for i in range(len(matrix)):
            self.bfs(i, 0, matrix, pacific_filled, 1)

        for i in range(len(matrix[0])):
            self.bfs(len(matrix)-1, i, matrix, atlantic_filled, -1)
        for i in range(len(matrix)):
            self.bfs(i, len(matrix[0])-1, matrix, atlantic_filled, -1)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pacific_filled[i][j] == True and atlantic_filled[i][j] == True:
                    res.append([i, j])
        return res

    def bfs(self, row, col, ocean, filled, pos):
        cur = ocean[row][col]
        filled[row][col] = True
        for dir in [[row+1, col], [row, col+1], [row-1, col], [row, col-1]]:
            x, y = dir[0], dir[1]
            if x >= len(ocean) or x < 0 or y >= len(ocean[0]) or y < 0:
                continue
            if ocean[x][y] >= cur and not filled[x][y]:
                self.bfs(x, y, ocean, filled, pos)

z = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(z.pacificAtlantic(heights))