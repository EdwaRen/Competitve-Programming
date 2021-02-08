class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        Use another stack of (char, freq) to track already seen characters
        """
        stack = [['/', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1]+=1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])

        res = []
        while stack:
            c, f = stack.pop(0)
            for i in range(f): res.append(c)
        return "".join(res)

z = Solution()
s = "pbbcggttciiippooaais"
k = 2
print(z.removeDuplicates(s, k))
