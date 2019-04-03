from random import randint
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        q = []
        heapq.heapify(q)

        for i in nums:
            heapq.heappush(q, i)
            if len(q) > k:
                heapq.heappop(q)
        return heapq.heappop(q)

        def partition(nums, lo, hi):
            streak = lo
            p = randint(lo, hi)
            print(p)
            for i in range(lo, hi):
                if nums[i] < nums[hi]:
                    nums[i], nums[streak] = nums[streak], nums[i]
                    streak+=1
            nums[streak], nums[hi] = nums[hi], nums[streak]
            return streak

        def quickselect(num, lo, hi, k):
            while True:
                if lo == hi:
                    return nums[lo]
                p = partition(nums, lo, hi)
                if k < p:
                    hi = p-1
                elif k > p:
                    lo = p+1
                else:
                    return nums[p]

        #return quickselect(nums, 0, len(nums)-1, len(nums)-k)

a = Solution()
b = [2, 1 ]
#b = [3, 2, 6, 1, 2, 4, 5, 6, 7, 3, 2, 6, 1, 2, 4, 5, 6, 7]
b = [3,2,1,5,6,4]
print(a.findKthLargest(b, 2))
