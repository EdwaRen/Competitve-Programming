import heapq

class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int

        Priority queue inspired solution where we maintain a heap of all
        previously seen speeds. We reverse sort all engineers by their efficiencies
        so that we start with the most efficient. As we go through more engineers,
        they will always be less efficient and we can update the answer by multiplying
        the current sliding sum by its efficiency.

        We track all previously seen speeds in a heap. If we have more than k
        elements in a heap, we pop the smallest. This heap does not necessarily contain
        the maximum performance but the cur_max will contain the max up to that point.
        """
        pq = []
        sliding_sum = 0
        cur_max = 0

        efficiencies = sorted(zip(efficiency, speed), reverse=True)
        for pairs in efficiencies:
            e, s = pairs[0], pairs[1]
            sliding_sum+=s
            heapq.heappush(pq, s)
            if len(pq) > k:
                sliding_sum -= pq[0]
                heapq.heappop(pq)
            cur_max = max(cur_max, sliding_sum*e)

        return cur_max%(10**9 + 7)

z = Solution()
n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 4
print(z.maxPerformance(n, speed, efficiency, k))
