class Solution(object):
    def getSum(self, a, b):

        # Handle edge case
        if a == 0:
            return b
        if b == 0:
            return a
       
        c = b

        # Masks cause It just be like that in Python
        # Python has an interesting way to represent integers since it doesn't use 32 bits rather, infinite bits
        # The solution is geared towards 32 bit answers so we need to accomodate for it
        mask = 0xFFFFFFFF
        min_int = 0x80000000
        max_int = 0x7FFFFFFF
 
        # Use half-adder method
        # Due to the nature of binary, we can replace b with c 
        while b != 0:

            # c identifies the carry bits
            c =( a & b) & mask

            # Perform XOR, now all we need to add is the carry bits
            # But the carry mights (once added) might create new carry bits, hence the while loop
            a = (a ^ b) & mask

            # Shift carry bits left
            b = (c << 1) & mask

        # Return negative case
        if a <= max_int:
            return a
        else:
            # Literally flip the bits twice, except we limit the first flip to 32 bits
            return ~(a ^ mask)

z = Solution()
a = -5
b = 5
print(z.getSum(a, b))


