import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Only squares have odd number of factors. Thus just return # of squares below n
        return int(math.sqrt(n))

z = Solution()
n = 1
print(z.bulbSwitch(n))
        
