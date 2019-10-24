import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Get Nth digit of a number
        def getNth(num, nth):
            return (num // (10**nth)) % 10

        # Catch edge case numbers
        if x < 0:
            return False

        if x == 0:
            return True

        # Take log of N
        N = int(math.log(x, 10))

        # Check every digit
        i = 0
        while i <= N:
            if getNth(x, i) != getNth(x, N-i):
                return False 
            i+=1

        return True
        
        
z = Solution()
n = 1111111121111111111111111111111111111111111111
print(z.isPalindrome(n))