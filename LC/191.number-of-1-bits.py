class Solution(object):
    def hammingWeight(self, n):

        # Use bit manipulation algorithm from Hamming Distance
        # n & (n-1) will remove the last (smallest) 1 bit while keeping the rest intact        
        res = 0
        while n:
            res += 1
            n = n & (n-1)
        return res    

z = Solution()
n = 512
print(z.hammingWeight(n))


 
