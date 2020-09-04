class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool

        The approach is similar to using a 2D matrix, where matrix[i][j]
        says that s1[:j] and s2[:i] has an existing combo. This is found by
        checking matrix[i-1][j] and matrix[i][j-1] and seeing if those
        respective combos are true. If so, we then check if [i] or [j] in s2/s1 
        matches s3[i+j-1].
        """
        if len(s1) + len(s2) != len(s3):
            return False

        # 1D DP array with extra slot in the beginning for Null character
        memo_list = [False for j in range(len(s1)+1)]
        memo_list[0] = True
        for i in range(len(s2)+1):
            for j in range(len(s1)+1):
                prev = memo_list[j]
                if j == 0 and i != 0:
                    memo_list[0] = True if memo_list[0] and s3[i-1] == s2[i-1] else False
                    continue

                # Fills based on previous dp to the left
                if j > 0 and memo_list[j-1] and s3[i+j-1] == s1[j-1]:
                    memo_list[j] = True 
                else:
                    # Fills based on previous dp to the top
                    if i > 0 and prev and s3[i+j-1] == s2[i-1]:
                        memo_list[j] = True
                    elif j > 0:
                        memo_list[j] = False

        return memo_list[-1] == True


z = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
s1 = "a"
s2 = "b"
s3 = "a"
s1 = "ab"
s2 = "bc"
s3 = "babc"
s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
s1 = ""
s2 = ""
s3 = "a"
# "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
# "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
# "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
print(z.isInterleave(s1, s2, s3))
