class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        This was quite difficult to understand, but basically I keep track of two substrings
        - i, j where i is the first substring
        - 'k' is the substring length of both i and j, used to reduce complexity of cases with 
        repeating characters

        The key to understanding this solution was `i = max(i+k+1, j)`

        When i is set to j, this case only occurs when all letters s[i:j] are smaller
        than s[j+k] otherwise the third conditional would have updated i, j, k

        When i is set to i+k+1, this means that i+k+1 > j which only occurs when there is 
        consistent overlap of letter such as aaaaaaaab. i+k+1 in this case would be the index of b.
        We are able to skip j because everything before i+k+1 is the same and s[j+k] must be the new
        maximum or else another conditional would have been visited
        """
        N = len(s)
        i, j, k = 0, 1, 0
        while j + k < N:
            if s[i+k] == s[j+k]:
                k+=1
                continue
            elif s[i+k] < s[j+k]:
                i = max(i+k+1, j)
                j = i + 1
            else:
                j = j+k+1
            k = 0
        return s[i:]
                

z = Solution()
s = "abab"
s = "leetcode"
s = "aaaaaaaab"
s = "cbaaaaacbab"
print(z.lastSubstring(s))