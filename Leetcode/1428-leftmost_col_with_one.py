# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        Traverse the matrix from the top right corner going down until the current column is zero 
        or all rows have been traversed. cur_r and cur_c represent the current index being queued
        and should point to a 0 exactly to the left of a 1.

        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        R, C = binaryMatrix.dimensions()
        cur_r, cur_c = 0, C-1
        
        while cur_r < R and cur_c >= 0:
            if binaryMatrix.get(cur_r, cur_c):
                if cur_c == 0:
                    return 0
                cur_c-=1
            else:
                cur_r+=1    

        return cur_c+1 if cur_c != C-1 else -1

z = Solution()

