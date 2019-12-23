class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        counter = 0
        res = []

        # Remove all extra closing brackets by not adding them to the return variable
        for letter in s:
            if letter == '(':
                counter += 1
                res.append(letter)
            elif letter == ')':
                if counter > 0:
                    counter -= 1
                    res.append(letter)
            else:
                res.append(letter)

        # Remove all extra opening brackets from the end first
        index = len(res)-1
        while counter > 0:
            if res[index] == '(':
                res.pop(index)
                counter -= 1
            index -= 1

        return ''.join(res)

z = Solution()
s = "(a(b(c)d)"
res = z.minRemoveToMakeValid(s)
print(res)
