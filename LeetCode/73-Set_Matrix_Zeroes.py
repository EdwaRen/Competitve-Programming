class Solution:
    def setZeroes(self, matrix):
        ver, hor = False, False
        for i in matrix:
            if i[0] == 0:
                ver = True

        for i in matrix[0]:
            if i == 0:
                hor = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # print("set outer zeroes", matrix)

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        # print("checked vertical zeroes", matrix)

        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        # print("checked horizontal zeroes", matrix)

        if ver:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if hor:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        matrix[:] = matrix
        # return matrix

a = Solution()
b = [
  [1,0,1, 1],
  [1,1,1,1],
  [1,1,0,1]
]
print(a.setZeroes(b))
print(b)
