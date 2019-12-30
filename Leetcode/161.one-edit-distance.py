import collections

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if s == t or s == None or t == None:
            return False

        # Assume s is always the smaller one
        if len(t) < len(s):
            t, s = s, t

        # Use separate pointers for each string
        j, i = 0, 0
        diff_count = 0
        while i < len(s):

            # Keep track of number of diffs
            if s[i] != t[j]:
                diff_count+=1
                if diff_count >= 2:
                    return False 
                # When len(t) > len(s)
                if len(s) != len(t):
                    i-= 1
            i+=1
            j+=1

        # Catch strings that are too long
        if j - diff_count + 1 < len(t):
            return False

        return True

z = Solution()
s = 'teacher'
t = 'teacherrr'
print(z.isOneEditDistance(s, t))        
