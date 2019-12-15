import math

class Solution(object):

    def kthSmallest(self, matrix, k):
        arr = []
        for i in matrix:
            arr += i    
        return sorted(arr)[k-1]
                


    def kthSmallest_binary_search(self, matrix, k):
        N = len(matrix)

        left = matrix[0][0]
        right = matrix[N-1][N-1]

        while left <= right:
            # Use binary search algorithm to find mid
            mid = math.floor( (left + right) /2 )
         
            # Count all elements less than mid in the entire matrix
            count = 0
            for row in matrix:
                j = 0

                # Count all elements less than mid in this row
                while j < len(row) and row[j] < mid:
                    j+=1
                count += j

            # Binary search repeat based on ultimate count
            if count < k:
                left = mid + 1
            else:
                right = mid -1
    
        return right

z = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

print(z.kthSmallest(matrix, k))


 
