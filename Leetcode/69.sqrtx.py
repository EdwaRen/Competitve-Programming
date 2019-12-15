class Solution(object):

    def mySqrt(self, x):

        # Use Newton's method       
        cur = x
        while cur*cur > x:
            cur = int((cur + (x/cur))/2)
        return int(cur)


z = Solution()
r = 20
print(z.mySqrt(r))


 
