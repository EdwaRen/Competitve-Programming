class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        # Create sparsed data structure that stores [[(index, value), ()]]
        # Basically a 2D array except each element is a tuple since the 
        #   matrix is sparse
        sparsed = []
        for row in range(len(B)):
            sparsed.append([])
            for col in range(len(B[0])):
                if B[row][col] != 0:
                    sparsed[row].append((col, B[row][col]))

        res = [[0 for i in range(len(B[0]))] for j in range(len(A))]

        # We iterate over the sparsed matrix so that we must perform an operation
        # at every step
        print("sparsed", sparsed)
        for row in range(len(B)):
            for col in range(len(sparsed[row])):
                for i in range(len(A)):
                    res[i][sparsed[row][col][0]] += A[i][row] * sparsed[row][col][1]

        return res

z = Solution()
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]
B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
A = [
    [0,1],
    [0,0],
    [0,1]
]
B = [
    [1,0],
    [1,0]
]
C = z.multiply(A, B)
print(C)
for i in C:
    for j in i:
        print(j, end=' ')
    print()




        
