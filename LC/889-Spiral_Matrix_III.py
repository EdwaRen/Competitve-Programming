class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        count = 0
        r = r0
        c = c0
        side = 1
        res = []

        while len(res) < R*C:
            neg = 1
            if side % 2 == 0:
                neg = -1

            for i in range(side):
                if r < R and r >= 0 and c < C and c >=0 :
                    res.append([r, c])
                c+=(1*neg)

            for i in range(side):
                if r < R and r >= 0 and c < C and c >=0 :
                    res.append([r, c])
                r+=(1*neg)

            side+=1
        return res[:(R*C)]
        
s = Solution()
R = 1
C = 4
r0 = 0
c0 = 0
print(s.spiralMatrixIII(R, C, r0, c0))
