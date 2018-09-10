import collections
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
        arr = collections.defaultdict(int)
        for i in s:
            arr[i]+=1
        for i in t:
            arr[i]-=1
        for i in s+t:
            if arr[i] != 0:
                return False
        return True
a = Solution()
b = "anagram"
c = "nagaram"
print(a.isAnagram(b, c))
