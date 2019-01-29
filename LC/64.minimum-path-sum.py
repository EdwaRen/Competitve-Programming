class Solution(object):
    def minPathSum(self, grid):
        r = len(grid)
        c = len(grid[0])
        row_sum = [0 for i in range(r)]
        column_sum = [0 for i in range(c)]
        row_sum[0] = column_sum[0] = grid[0][0]
        for i in range(1, r):
            row_sum[i] += row_sum[i-1] + grid[i][0]
        for j in range(1, c):
            column_sum[j] += column_sum[j-1] + grid[0][j]
        	
#        print('init sums', row_sum, column_sum)
        for i in range(1, r):
            for j in range(1, c):
                row_sum[i] = min(row_sum[i], column_sum[j]) + grid[i][j]
                column_sum[j] = row_sum[i]
 #       print("sums", row_sum, column_sum)
        return column_sum[c-1]

a = Solution()
arr = [
[1]
#    [1, 3, 1, 1]
#    [1, 5, 10, 2],
#    [4, 2, 1, 1]

]
print(a.minPathSum(arr))
        
