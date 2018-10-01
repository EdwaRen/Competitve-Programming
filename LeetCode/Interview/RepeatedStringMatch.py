import math


class Solution:
    def repeatedStringMatch(self, A, B):
        t = int(math.ceil(len(B)/len(A)))
        for i in range(0, 2):
            extend = A*(t+i)
            if B in extend:
                return t +i
        return -1

a = Solution()
b = "abc"
c = "abcabca"
b = "aa"
c = "a"
print(a.repeatedStringMatch(b, c))
