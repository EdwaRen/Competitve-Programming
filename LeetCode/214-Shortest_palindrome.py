class Solution:

    def shortestPalindrome(self, s):
        kmp = [0] * len(s+ "#" + s[::-1])
        big_s = s + "#" + s[::-1]
        def kmp_set():
            for i in range(1, len(big_s)):
                t = kmp[i-1]
                while t > 0 and big_s[i] != big_s[t]:
                    t = kmp[t-1]
                if big_s[i] == big_s[t]:
                    t+=1
                kmp[i] = t
        kmp_set()
        palin = s[:kmp[-1]]
        prefix = s[kmp[-1]:]
        return (prefix[::-1] + palin + prefix)

a = Solution()
b = "abcd"
print(a.shortestPalindrome(b))
