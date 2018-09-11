import collections

class Solution():
    def partitionLabels(self, nums):
        dict = {c:i for i, c in enumerate(nums)}
        cur = 0
        start = 0
        res = []
        for i, j in enumerate(nums):
            cur = max(cur, dict[j])
            if i == cur:
                res.append(1+cur-start)
                start = cur+1
        return res

a = Solution()
b = "ababcbacadefegdehijhklij"
print(a.partitionLabels(b))
