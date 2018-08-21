from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums, k):
        q = PriorityQueue()
        res = 0
        for i in nums:
            q.put((-i, i))
        for i in range(k):
            res = q.get()[1]
        return res

a = Solution()
b = [3, 2, 1, 5, 6, 4, ]
#b = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(a.findKthLargest(b, 2))
