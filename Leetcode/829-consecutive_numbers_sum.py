class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # start off with N = N as a possibility
        res = 1
        # i is the number of elements in a consecutive chunk
        i = 2
        while i*(i+1)//2 <= N:
            # n0 is the smallest consecutive sum with i elements
            if (N - ((i)*(i+1)//2)) % i == 0:
                res += 1
            i += 1
        return res 

z = Solution()
N = 15
print("ans", z.consecutiveNumbersSum(N))