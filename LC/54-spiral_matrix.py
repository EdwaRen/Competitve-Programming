class Solution:
    def spiralOrder(self, matrix):
        res = []
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])
        r1 = 0
        r2 = n-1
        c1 = 0
        c2 = m-1
        i = 0
        j = 0
        while len(res) < m * n and r2 >=0 and c2 >=0:
            i = r1
            while i <= r2:
                res.append(matrix[c1][i])
                i+=1
            c1+=1
            j = c1
            if len(res) < m * n:
                while j <= c2:
                    res.append(matrix[j][r2])
                    j+=1
                r2-=1
            if len(res) < m * n:
                i = r2
                while i >= r1:
                    res.append(matrix[c2][i])
                    i-=1
                c2-=1
            if len(res) < m * n:
                j = c2
                while j >= c1:
                    res.append(matrix[j][r1])
                    j-=1
                r1+=1
        return res


a = Solution()
matrix = [
  [1]
]
print(a.spiralOrder(matrix))
