class Solution(object):
    def maximalSquare(self, matrix):
        # Handle edge case
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        # Record length of edge of the max-sized square
        square_max = int(matrix[0][0])

        # The dp array is named 'arr'
        arr = []

        # Set initial values of arr
        for i in range(len(matrix[0])):
            arr.append(int(matrix[0][i]))
            if arr[-1] > square_max:
                square_max = arr[-1]        
        
        # Iterate through every value of the matrix
        for i in range(1, len(matrix)):
              
            # Set initial variables before inner loop
            # Temp tracks upper left square size, arr[j] the upper suqare, and arr[j-1] the left square
            temp = arr[0]
            arr[0] = int(matrix[i][0])
            if arr[0] > square_max:
                square_max = arr[0]

            # Updates arr with previous values on every iteration
            for j in range(1, len(matrix[0])):
                temp_new = arr[j]
                if matrix[i][j] == "1":
                    arr[j] = min(arr[j], arr[j-1], temp) +1
                else:
                    arr[j] = 0
                
                # Reset temp, temp tracks the upper_left square
                temp = temp_new
                if arr[j] > square_max:
                    square_max = arr[j]

        return square_max*square_max


#        """
#        :type matrix: List[List[str]]
#        :rtype: int
#        """

z = Solution()
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

_matrix = [
    ["1","0","1","1","1"],
    ["0","1","0","1","0"],
    ["1","1","0","1","1"],
    ["1","1","0","1","1"],
    ["0","1","1","1","1"]]

_matrix = [
    ["0","0","0","0","0"],
    ["1","0","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"]
]

_matrix = [
    ["0", "0"]
]
print(z.maximalSquare(matrix))
