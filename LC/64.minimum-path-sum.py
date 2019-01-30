class Solution(object):
    def minPathSum(self, grid):
        """
        Solution that uses O(m) space
        Uses an array the length of a row to store every sum above cell in question.
        Array[0] in this case is the sum of the 0th element of the next row
        Checks for sum above and below (arr[i-1], arr[i]) which is updated after every iteration
        """        

        r = len(grid)
        c = len(grid[0])
        
        # Inits column sum array (row sum works as well)
        col_sum = [0 for i in range(c)]
        col_sum[0] = grid[0][0]
        
        # Defaults col_sum to be the sum of the first element of every column (horizontal summing)
        for j in range(1, c):
            col_sum[j] += col_sum[j-1] + grid[0][j]        
        
        # Iterates through the grid
        for i in range(1, r):
            # Updates to be the first element of the next row
            col_sum[0] += grid[i][0]

            # Updates col_sum for each remaining element of this row
            for j in range(1, c):
                col_sum[j] = min(col_sum[j-1], col_sum[j]) + grid[i][j]
        
        return col_sum[-1]
                

    def minPathSum_two_arr(self, grid):
        """
        Uses two array approach instead of O(mn) space
        Sums are consistenly updated after every traversal

        """
        r = len(grid)
        c = len(grid[0])

        # Create DP array
        row_sum = [0 for i in range(r)]
        column_sum = [0 for i in range(c)]

        # Init first element of DP array
        row_sum[0] = column_sum[0] = grid[0][0]

        # Setup the initial values of the sum_arrays
        for i in range(1, r):
            row_sum[i] += row_sum[i-1] + grid[i][0]
        for j in range(1, c):
            column_sum[j] += column_sum[j-1] + grid[0][j]

        # Iterate through the entire grid        	
        for i in range(1, r):
            for j in range(1, c):
                # Looks at space above and to the left, finds the min and adds current grid value
                row_sum[i] = min(row_sum[i], column_sum[j]) + grid[i][j]
                
                # Updates column part of grid[i][j]                
                column_sum[j] = row_sum[i]

        # return row_sum[r-1] also works
        return column_sum[c-1]

a = Solution()
arr = [
#[1]
    [1, 3, 1, 1],
    [1, 5, 10, 2],
    [4, 2, 1, 1]

]
print(a.minPathSum(arr))
        
