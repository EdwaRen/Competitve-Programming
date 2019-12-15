class Solution(object):
    def titleToNumber(self, s):
        # Convert a charcter to it's 26 indexed representation
        def to_int(char):
            return ord(char) - 64

        # Iterate and sum all based on base 26
        res = 0
        for i in range(len(s)):
            power = len(s) - i -1
            mult = 26 ** power
            res += to_int(s[i]) * mult

        return res

z = Solution()
s = "ZY"
print(z.titleToNumber(s))
 
