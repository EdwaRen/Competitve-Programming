class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        N = len(matrix)
        M = len(matrix[0])
        
        prefix_sums = [0 for i in range(N)]
        for row in range(matrix):
            for col in range(matrix[0]):
                