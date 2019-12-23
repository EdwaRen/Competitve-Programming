import collections

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        map1 = collections.defaultdict(int)
        res = 0

        for i in A:
            for j in B:
                map1[i + j]+=1

        for i in C:
            for j in D:
                res += map1[0 - (i+j)] 

        return res

z = Solution()
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(z.fourSumCount(A, B, C, D))



 
