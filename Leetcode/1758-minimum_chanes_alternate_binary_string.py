class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int

        Easy solution:
        zero_start, one_start, odd = 0, 0, True
        for c in s:
            is_zero = int(i)%2
            if c == '1' and odd: one_start += 1
            elif c == '0' and odd: zero_start += 1
            elif c == '1' and not odd: zero_start += 1
            elif c == '0' and not odd: one_start += 1          
            odd = not odd  

        More elegant solution using a single loop and comparison
        """
        differences = sum( ind % 2 == int(val) for ind, val in enumerate(s))
        return min(differences, len(s) - differences)

z = Solution()
s = "1111"
print(z.minOperations(s))