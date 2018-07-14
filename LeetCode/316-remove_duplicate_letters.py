class Solution:
    def removeDuplicateLetters(self, s):
        for c in sorted(set(s)):
            chop = s[s.index(c):]
            # print(c, set(chop), set(s), chop, c, s)
            if set(chop) == set(s):
                return c + self.removeDuplicateLetters(chop.replace(c, ""))
        return ""
a = Solution()
b = "cbabc"
print(a.removeDuplicateLetters(b))
