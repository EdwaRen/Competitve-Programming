import math
class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, math.ceil(n ** 0.5)):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        return sum(primes)

a = Solution()
b = 12
print(a.countPrimes(b))
