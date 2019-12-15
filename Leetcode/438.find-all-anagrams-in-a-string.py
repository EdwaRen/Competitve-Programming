class Solution(object):
    def findAnagrams(self, s, p):
        palin_dict = [0] * 26
        for i in p:
            palin_dict[ord(i) %26] +=1
#        print("palin_dict", palin_dict)

        res = []
        for i in range(len(s)):
            palin_dict[ord(s[i])%26] -=1
            if i >= len(p):
                palin_dict[ord(s[i-len(p)])%26] +=1
            if len(set(palin_dict)) == 1 and (palin_dict)[0] == 0:
                res.append(i-len(p)+1)
 #           print("set palindict", palin_dict)

        return res

z = Solution()
s = "cbaebabacd"
p = "abc"
print(z.findAnagrams(s, p))
