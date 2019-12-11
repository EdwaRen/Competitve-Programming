class Solution(object):
    def divide(self, dividend, divisor):

        # Handle negatives
        neg = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Track cur_div which are bitshifted multiples of the divisor
        cur_div = divisor

        res = 0
        remainder = dividend

        # Loop while we can still divide remainder by divisor
        while remainder >= divisor:

            # Reset cur_div to be the divisor
            cur_div = divisor
            count = 1

            # bitshift cur_dev to the left while it is less than the remainder
            while cur_div <= remainder:
                remainder -= cur_div
                res += count

                # bitshifts, count will keep track of the amount of shifting so we add it to the res variable
                cur_div = cur_div << 1
                count <<= 1

        # Detect negatives
        if neg:
            return max(-res, -2**31)
        return min(res, (2**31)-1)

z = Solution()
dividend = -10
divisor = -3
print(z.divide(dividend, divisor))





