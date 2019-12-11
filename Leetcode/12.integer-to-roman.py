class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Map for values to numerals
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ''
        count = 0
        while num:
            res += (num//values[count]) * numerals[count]
            num = num%values[count]
            count += 1
        return res

z = Solution()
num = 99
print(z.intToRoman(num))