import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        [1, 2], [2, 3], [3, 8], [1, 3]
        Sort events then greedily use a PQ. O(nlogn)
        Start from day 0 but jump to earliest date with event
        Push end date to PQ of all events that start on that day
        Add the event that ends the earliest as a result (res+=1)
        Increment the current day, repeat from start until the PQ is empty
        which then means to jump again to the next date with an event.
        """

        events = sorted(events, key=lambda x: (x[0]))
        pq = []
        res = 0
        event_ind = 0 
        day = 0
        while event_ind < len(events) or pq:
            if not pq:
                day = events[event_ind][0]

            while event_ind < len(events) and events[event_ind][0] <= day:
                heapq.heappush(pq, events[event_ind][1])
                event_ind+=1

            while pq and pq[0] < day:
                heapq.heappop(pq)

            if pq and day <= pq[0]:
                heapq.heappop(pq)
                res+=1

            day+=1

        return res

z = Solution()
events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
events = [[1,2],[1,2],[2,2],[1,5],[1,5]]
# events = [[1,5],[1,5],[1,5],[2,3],[2,3]]
print(z.maxEvents(events))
            
        