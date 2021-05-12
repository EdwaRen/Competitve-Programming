class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        Generate so that two sides will add up to 1
        """
        even = True if (n%2 == 0) else False
        lo = (n/2)
        res = []
        if not even: res.append(0)
        for i in range(1, lo+1):
            res.append(-i)
            res.append(i)
        return res 

z = Solution()
n = 5
print(sum(z.sumZero(n)))
