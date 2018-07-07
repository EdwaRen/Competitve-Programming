class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and (10460353203 / n) % 1 == 0
