class Solution(object):
    def romanToInt(self, s):
        conv = {"I":1, "V": 5, "X": 10, 'L':50, 'C':100, 'D':500, 'M':1000}
        temp = conv[s[0]]
        result = 0
        for i in range(1, len(s)):
            if conv[s[i]] > conv[s[i-1]]:
                result += conv[s[i]] - temp
                temp = 0
            else:
                result +=  temp
                temp = conv[s[i]]
        return result + temp

a = Solution()
b = "I"
print(a.romanToInt(b))
