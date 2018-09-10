class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min = 999999999
        minword = ""
        for i in strs:
            if len(i) < min:
                min = len(i)
                minword = i
        res = ""
        for i in range(min):
            for j in strs:
                if j[i] != minword[i]:
                    return res
            res+= minword[i]
        return res


a = Solution()
b = ["flowe"]
print(a.longestCommonPrefix(b))
