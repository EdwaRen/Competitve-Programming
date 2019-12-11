class Solution(object):
    def hammingDistance(self, x, y):
        xor = x ^ y
        count = 0
        
        while xor:
            xor = xor & (xor - 1)
            count +=1

        return count

z = Solution()
a = 1
b = 4
print(z.hammingDistance(a, b))

    


