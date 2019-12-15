class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            A[i] = reversed(A[i])
            A[i] = [int(not k) for k in A[i]]
        return A[:]

a = Solution()
b  = [[1,1,0],[1,0,1],[0,0,0]]
b = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(a.flipAndInvertImage(b))
