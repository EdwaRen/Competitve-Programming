import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))

z = Solution()
n = 1
print(z.bulbSwitch(n))
        
