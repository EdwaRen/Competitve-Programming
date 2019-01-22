class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.recurse(s)[0]

    def recurse(self, word):
        res = ""
        factor = 0
        index = 0
        while index < len(word):

            if word[index].isdigit():
                factor *= 10
                factor += int(word[index])
            else:
                if word[index] == '[':
                    index+=1
                    req = self.recurse(word[index:])
                    if factor == 0:
                        factor = 1
                    for i in range(factor):
                        res+=(req[0])
                    index += req[1]
                    factor = 0
                elif word[index] == ']':
                    return (res, index)
                else:
                    res+= word[index]
            index+=1
        return (res, index)

a = Solution()
print(a.decodeString("2[abc]3[cd]ef"))
