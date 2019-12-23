# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
    

       
def isBadVersion(version):
    if version < self.bad:
        return False
    return True


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        hi = n
        lo = 1
        
        while lo < hi:
            m = lo + ((hi - lo) // 2)
            if isBadVersion(m):
                hi = m
            else:
                lo = m + 1
        return lo

z = Solution()
n = 4
bad = 1
res = z.firstBadVersion(n, bad)
print(res)

