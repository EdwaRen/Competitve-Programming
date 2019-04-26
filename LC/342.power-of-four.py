class Solution(object):
    def isPowerOfFour(self, num):
       
        # One dig to detect if there is exactly a single 1 in the binary representation of n
        one_dig = not (num&(num-1))

        # the following number is 0x5555555555 in decimal form
        divisible_by_four = num & 93824992236885
     
        return bool(one_dig and divisible_by_four)

z = Solution()
num = 2562
print(z.isPowerOfFour(num))
