class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # Get diagonal going northest
        def north_east(row, col, matrix, diag):
            while row >= 0 and col < len(matrix[0]):
                diag.append(matrix[row][col])
                row -=1
                col+=1

        res = []
        row = 0
        col = 0
        count = 0

        # Generate the sequence for every possible diagonal.
        while row != len(matrix) and col != len(matrix[0]):
            diag = []
            north_east(row, col, matrix, diag)

            # Reverse every alternating diagonal
            diag = diag[::-1] if count % 2 == 1 else diag
            res += diag 

            # Handle the edge corner curve
            if row + 1< len(matrix):
                row += 1
            else:
                col += 1
            count += 1
        return res
            
nums = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ]
#  [ 7, 8, 9 ]
]

z = Solution()
print(z.findDiagonalOrder(nums))