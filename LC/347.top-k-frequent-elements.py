import collections
import queue as Q

class Solution(object):
    def topKFrequent(self, nums, k):
        res = []
        dic = collections.defaultdict(lambda:0)
        for i in nums:
            dic[i]+=1
        buckets = collections.defaultdict(lambda:[])

        for i in nums:
            if i not in buckets[dic[i]]:
                buckets[dic[i]].append(i)

        for i in range(len(nums)):
            reverse_i = len(nums)-i
            for j in buckets[reverse_i]:
                res.append(j)

        return res[:k]

    def topKFrequent_old(self, nums, k):
        res = []
        dic = collections.defaultdict(lambda:0)
        for i in nums:
            dic[i]+=1

        q = Q.PriorityQueue()
        for i in set(nums):
            q.put((-1*dic[i], i))

        for i in range(k):
            res.append(q.get()[1])
        return res

a = Solution()
print(a.topKFrequent([1, 1, 1, 2, 2, 3], 2))
