class Solution(object):
    def isHappy(self, n):
        
        # Calculate next num based off sum of squares of digits
        def next(num):
            happy = 0
            while num > 0:
                digit = num % 10
                happy += digit * digit
                num = int(num/10)
            return happy

        # Use the walker/runner method to detect a cycle
        walk = n
        run = next(n)

        if walk == run:
            return True

        # Loop until either walk or run hits 1, or a loop is detected
        # Same algorithm as in detecting a cyclical linkedlist
        while walk != run:
            if walk == 1 or run == 1:
                return True
            walk = next(walk)
            run = next(next(run))

        return False

z = Solution()
n = 20
print(z.isHappy(n))




