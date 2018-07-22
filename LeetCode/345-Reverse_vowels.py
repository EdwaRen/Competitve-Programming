class Solution(object):
    def reverseVowels(self, s):
        start = 0
        end = len(s)-1
        vowels = "aeiouAEIOU"
        res = list(s)
        while start < end:
            while start < end and res[start] not in vowels:
                start +=1
            while start < end and res[end] not in vowels:
                end-=1
            temp = res[start]
            res[start] = res[end]
            res[end] = temp
            start+=1
            end-=1


        return "".join(res)

    def reverseVowels_old(self, s):
        chars = []
        pos = []
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                chars.append(s[i])
                pos.append(i)
        rev = pos[::-1]
        res = list(s)
        for i in range(len(rev)):
            res[rev[i]] = chars[i]

        return "".join(res)

a = Solution()
b = 'leetcode'
print(a.reverseVowels(b))
