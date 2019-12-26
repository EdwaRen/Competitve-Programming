class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """

        a_count = 1
        res = ""
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        # Simple logic
        for i in S.split(' '):
            if i[0] in vowels:
                res += i+'ma'+('a'*a_count)+' '
            else:
                res += i[1:]+i[0]+'ma'+('a'*a_count)+' '
            a_count+=1
        return res[:-1]

z = Solution()
S = "The quick brown fox jumped over the lazy dog"
print(z.toGoatLatin(S))

        
