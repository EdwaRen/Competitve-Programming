class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        if matrix == None or len(matrix) == 0:
            return None
        
        self.cum_sums = [ [0] + i for i in  matrix]
        self.cum_sums.insert(0, [0 for i in range(len(matrix[0])+1)])

        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                self.cum_sums[i][j] = matrix[i-1][j-1] + self.cum_sums[i-1][j] + self.cum_sums[i][j-1] - self.cum_sums[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row2 < row1 or col2 < col1:
            return 0
        return self.cum_sums[row2+1][col2+1] - self.cum_sums[row1][col2+1] - self.cum_sums[row2+1][col1] + self.cum_sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2,1,4,3)
param_1 = obj.sumRegion(1,2,2,4)

print(param_1)