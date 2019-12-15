class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Bit manipulation, adds the last digit of n, then reduces n by a bit so that
        # it is added to res in reverse
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)  
            n = n >> 1
        return res


z = Solution()
num = 11
print(z.reverseBits(num))


      
