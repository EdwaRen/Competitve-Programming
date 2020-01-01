import heapq 

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """

        # Guard against edge cases
        if not sticks or len(sticks) <= 1: return 0 

        # Save sticks to a heap (Priority queue)
        heap = sticks
        heapq.heapify(heap)
        res = 0

        # Keep popping smaller item, then add the combined one back in
        for _ in range(len(sticks)-1):
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            res += x + y 
            heapq.heappush(heap, x+y)
            
        return res 

z = Solution()
sticks = [5]
print(z.connectSticks(sticks))