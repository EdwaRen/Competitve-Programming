class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Double binary search, applied the DRY principle by passing in conditions
        to the binary search algorithm instead of having 2 very similar functions
        """
        col = self.binary_search(matrix, -2, target, self.colSearchCondition)
        return self.binary_search(matrix, col, target, self.rowSearchCondition)

    def binary_search(self, matrix, col, target, rowCondition):
        lo = 0
        hi = len(matrix)-1 if col == -2 else len(matrix[0])-1

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if target < rowCondition(matrix, col, mid):
                hi = mid - 1
            elif target > rowCondition(matrix, col, mid):
                lo = mid + 1
            elif target == rowCondition(matrix, col, mid):
                return mid if col == -2 else True

        return min(lo, hi) if col == -2 else False
    
    def colSearchCondition(self, matrix, col, mid):
        return matrix[mid][0]

    def rowSearchCondition(self, matrix, col, mid):
        return matrix[col][mid]


z = Solution()
matrix = [[1, 3]]
target = 3
print(z.searchMatrix(matrix, target))
