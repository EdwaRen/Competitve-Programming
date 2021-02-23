class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int

        For every character, we calculate the number of instances
        that it is a single unique char in a string. This only occurs
        between the last 2 occurrences of the character, any more and it
        will not be a single unique char.
        """

        letters = [[-1, -1] for i in range(26)]
        res = 0
        for i in range(len(s)):
            letter = ord(s[i]) % 26
            m, n = letters[letter]
            res += (n - m) * (i-n)
            letters[letter][0] = n
            letters[letter][1] = i

        for i in letters:
            res += (i[1] - i[0]) * (len(s) - i[1])

        return res % (10**9 + 7)

z = Solution()
s = "ABC"
s = "ABA"
s = "LEETCODE"
print(z.uniqueLetterString(s))
