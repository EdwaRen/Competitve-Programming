class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        N = len(A)
        countsA = [0 for i in range(6)]
        countsB = [0 for i in range(6)]
        intersects = [0 for i in range(6)]

        for i in range(len(A)):
            countsA[A[i]-1] +=1
            countsB[B[i]-1] +=1

            if A[i] == B[i]:
                intersects[A[i]-1]+=1

        valids = []
        for i in range(6):
            if countsA[i] + countsB[i] - intersects[i] == N:
                valids.append(N-max(countsA[i], countsB[i]))
        if len(valids) == 0:
            return -1
        return min(valids)
        
        
z = Solution()
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
print(z.minDominoRotations(A, B))