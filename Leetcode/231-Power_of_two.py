class Solution:
    def isPowerOfTwo(self, n):
        if n < 0:
            return False
        return n&(n-1) == 0

    # Alternative, more general solution involving max values of unsigned ints
    def isPowerOfTwo_V2(self, n):
        return n > 0 and (2^30 % n == 0)

a = Solution()
n = 31
print(a.isPowerOfTwo(n))
