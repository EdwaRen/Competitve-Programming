class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        cur = 5

        while n >= cur:
            res += (n/cur) 
            cur *= 5

        return res

z = Solution()        
n = 124
print(z.trailingZeroes(n))
