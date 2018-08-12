from collections import defaultdict

class Solution(object):
    def uncommonFromSentences(self, A, B):
        A_list = A.split()
        B_list = B.split()
        map = {}
        map = defaultdict(lambda:0, map)
        for i in A_list:
            map[i] +=1
        for i in B_list:
            map[i] +=1

        res = []
        for i in (A_list + B_list):
            if map[i] == 1:
                res.append(i)
        return res

a = Solution()
b = "apple apple"
c = "banana"
print(a.uncommonFromSentences(b, c))
