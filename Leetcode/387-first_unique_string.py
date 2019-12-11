from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        s_dict = defaultdict(int)
        for i in s:
            s_dict[i]+=1
        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                return i
        return -1
s = "loveleetcode"
a = Solution()
print(a.firstUniqChar(s))
