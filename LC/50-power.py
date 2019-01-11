import pprint

class Solution:

    def power_sqr(self, x, n):
        if n <= 0:
            return 1.00
        half_sqr = self.power_sqr(x, n/2)
        if n %2 == 0:
            return half_sqr * half_sqr
        else:
            return half_sqr * half_sqr * x

    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -n
        return self.power_sqr(x, n)

a = Solution()
print(a.myPow(2.0000000, 10))
