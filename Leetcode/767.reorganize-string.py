from collections import defaultdict

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        d = defaultdict(int)
        max_bucket = 0
        max_char = 'a'
        
        for c in S:
            d[c] += 1
            if d[c] >= max_bucket:
                max_bucket = d[c]
                max_char = c

            if d[c] > (len(S) + 1) / 2:
                return ''
            
        del d[max_char]
        frequencies = d.items()

        res = ['' for i in range(len(S))]
        index = 0

        for i in range(max_bucket):
            res[index] = max_char
            index += 2

        for pair in frequencies:
            for _ in range(pair[1]):
                if index >= len(S):
                    index = 1
                res[index] = str(pair[0])
                index += 2

        return ''.join(res)

        
        
        
z = Solution()
res = z.reorganizeString('aabab')
print(res)