from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        d = deque()
        res = []
        for index, value in enumerate(nums):
            while d and nums[d[-1]] < value:
                d.pop()
            d.append(index)
            if d[0] == index-k:
                d.popleft()
            if index > k-2:
                res.append(nums[d[0]])
        return res

a = Solution()
b = [1,3,-1,-3,5,3,6,7]
k = 3

print(a.maxSlidingWindow(b, k))
