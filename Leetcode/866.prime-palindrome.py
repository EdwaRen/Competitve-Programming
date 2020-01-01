import math

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

        # Check if prime using the sqrt method
        def isPrime(n):
            if n <= 1: return False 
            if n == 2: return True 

            for i in range(2, int(math.sqrt(n))+1):
                if n%i == 0:
                    return False 
            return True

        # Continue while digits <= 9, since 10^8 is less than 9 digits long
        digits = len(str(N))
        while digits <= 9:
            root = digits // 2

            # Check single length
            if digits == 1:
                for candidate in range(12):
                    if candidate >= N and isPrime(candidate):
                        return candidate

            if digits <= 2:
                # Check for even length palindrone first
                for i in range(10**(root-1), 10**root):
                    candidate = int(str(i) + str(i)[::-1])
                    if candidate >= N and isPrime(candidate):
                        return candidate

            # Check for odd length next (Odd is always bigger)
            for i in range(10**(root-1), 10**(root)):
                for j in range(10):
                    candidate = int(str(i) + str(j) + str(i)[::-1])
                    if candidate >= N and isPrime(candidate):
                        return candidate
            digits += 1

        

z = Solution()
N = 101101
print(z.primePalindrome(N))
