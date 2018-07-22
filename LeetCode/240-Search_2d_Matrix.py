class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return False
        r = 0
        c = len(matrix[0])-1
        while r < len(matrix) and c >= 0 and matrix[r][c] != target:
            while c >=0 and matrix[r][c] > target:
                c-=1
            while r < len(matrix) and matrix[r][c] < target:
                r+=1
        return r < len(matrix) and c >= 0 and matrix[r][c] == target

a = Solution()
b = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(a.searchMatrix(b, 21))
