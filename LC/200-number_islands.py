import Queue


class Solution(object):
    def numIslands(self, grid):
        q = Queue.Queue()
        islands = 0
        for r in range(len(grid)):
            for i in range(len(grid[r])):
                if grid[r][i] =="1":
                    islands+=1
                    q.put([r, i])
                while not q.empty():
                    cur = q.get()
                    row = cur[0]
                    col = cur[1]
                    if row-1 >= 0 and grid[row-1][col] == "1":
                        q.put([row-1, col])
                        grid[row-1][col] = "0"
                    if row+1 < len(grid) and grid[row+1][col] == "1":
                        q.put([row+1, col])
                        grid[row+1][col] = "0"
                    if col - 1 >= 0 and grid[row][col-1] == "1":
                        q.put([row, col-1])
                        grid[row][col-1] = "0"
                    if col+1 < len(grid[row]) and grid[row][col+1] == "1":
                        q.put([row, col+1])
                        grid[row][col+1] = "0"
        return islands

a = Solution()
#print(a.numIslands([["1", "1", 1, 1, 0],[1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0] ]))
print(a.numIslands([["1", "1", "0", "0", "0"],["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"] ]))
