import collections

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """

        # Start from the back, and use Euclidean's algorithm
        # if d > c, d%c is guaranteed to return the only new d which is less than c
        # If we trace the operations form the back, each possibility appears at least once as either c or d
        # --> This means we only need to check a == c rather than also b == d
        def recurse(a, b, c, d):
            if c < a:
                return False
            elif a == c:
                return ((d - b) % a) == 0
            else:
                return recurse(b, a, d%c, c)
            
        if tx < sx or ty < sy:
            return False
        if tx < ty:
            return recurse(sx, sy, tx, ty)
        else:
            return recurse(sy, sx, ty, tx)

z = Solution()
sx = 3
sy = 7 
tx = 3
ty = 4
# sx = 35
# sy = 13
# tx = 455955547
# ty = 420098884

print(z.reachingPoints(sx, sy, tx, ty))