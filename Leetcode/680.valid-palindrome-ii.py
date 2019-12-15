class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def check_palin(a, b):
            return a == a[::-1] or b == b[::-1]

        l = 0 
        r = len(s)-1
        while s[l] == s[r] and l < r:
            l+=1
            r-=1
        if s[l] != s[r]:
            return check_palin(s[l:r], s[l+1: r+1])
        return True


z = Solution()
s = 'aaaaaaaaaba'
print(z.validPalindrome(s))
        
