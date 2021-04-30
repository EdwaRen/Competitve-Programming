from itertools import groupby

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        Solution 1) Brute force generation:

            res = '1'
            for i in range(1, n):
                count = 1
                updated_res = ''
                for j in range(len(res)):
                    if j+1 < len(res) and res[j] == res[j+1]:
                        count+=1
                    else:
                        updated_res += str(count) + res[j]
                        count = 1
                res = updated_res
            return res

        Solution 2) Using Python's Itertools.groupby function:
        """

        res = '1'
        for _ in range(1, n):
            updated_res = ''
            for k, v in groupby(res):
                updated_res += str(len(list(v))) + str(k)
            res = updated_res
        return res

z = Solution()
n = 6
print(z.countAndSay(n))


