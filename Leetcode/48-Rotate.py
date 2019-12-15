class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]



a = Solution()
b = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
(a.rotate(b))
print(b)
