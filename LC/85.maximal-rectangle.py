class Solution(object):
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0

        # Index of the leftmost part of the rectangle that goes up until the current height
        left_arr = [0] * len(matrix[0])

        # Index of the height
        height_arr = [0] * len(matrix[0])

        # Index of the rightmost part of the rectangle that goes up until the current height
        right_arr = [len(matrix[0])] * len(matrix[0])

        # Maximum area of the rectangle
        max_area = 0        
        
        
        for i in range(len(matrix)):
            # Define starting positions for each row
            left_start = 0
            right_start = len(matrix[0])                                

            # Update left_arr
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    left_arr[j] = max(left_arr[j], left_start)
                    height_arr[j] += 1
                else:
                    left_arr[j] = 0
                    left_start = j + 1    
                    height_arr[j] = 0    

            # Update right_arr
            for k in range(len(matrix[0])):
                j = len(matrix[0]) - 1 - k
                if matrix[i][j] == "1":
                    right_arr[j] = min(right_arr[j], right_start)
                else:
                    right_arr[j] = len(matrix[0])
                    right_start = j                

            # Compute max rectangle
            for j in range(len(matrix[0])):
                max_area = max(max_area, (right_arr[j] - left_arr[j])*height_arr[j])

        return max_area


z = Solution()
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(z.maximalRectangle(matrix))        
