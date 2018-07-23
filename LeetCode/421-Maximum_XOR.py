class Solution(object):
    def findMaximumXOR(self, nums):
        max = 0
        mask = 0
        for k in xrange(30, -1, -1)
            prefix = set()
            mask |= 1 << k
            for i in nums:
                prefix.add(i&mask)
            try_max = max | 1 << k
            for i in prefix:
                if try_max ^ i in prefix:
                    max = try_max
                    break
        return max

a = Solution()
b = [3, 10, 5, 25, 2, 8]
# b = [8, 10, 2]
print(a.findMaximumXOR(b))
