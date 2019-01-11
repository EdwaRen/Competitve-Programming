import math

class Solution:
    def numSquares(self, n):
        if n < 1:
            return n
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i+=1

        count = 0
        queue = set([n])
        while queue:
            count+=1
            ls = set()
            for i in queue:
                for j in squares:
                    if i == j:
                        return count
                    elif i < j:
                        break
                    ls.add(i-j)
            queue = ls
        return count


a = Solution()
print(a.numSquares(13))
