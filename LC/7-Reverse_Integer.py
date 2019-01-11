import math
class Solution:
    def reverse(self, x):
        res = 0
        neg = 1
        if x < 0:
            neg = -1
        x = abs(x)
        while True:
            if x < 10:
                res = res*10 + x%10
                break
            else:
                res = res*10 + x%10
                x = int(math.floor(x/10))
        res = res*neg
        if res > 2**31-1 or res < -2**31:
            return 0
        return res

a = Solution()
b = -1231231231232131
print(a.reverse(b))
