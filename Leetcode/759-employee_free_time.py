"""
# Definition for an Interval.

"""
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

import heapq

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]

        Put K (number of employees) into the heap. Since the employees are
        already sorted, putting the first interval of each employee will
        guarantee that the min element is in the heap.

        When popping the heap, we keep track of the prev_max which is the largest
        endtime seen so far.
        """
        # for idx, emp in schedule:
        #     print(emp[0])
        pq = [(emp[0].start, idx, 0) for idx, emp in enumerate(schedule)]
        heapq.heapify(pq)
        prev_max = min(emp.start for avails in schedule for emp in avails)
        res = []
        while pq:
            start, idx, col = heapq.heappop(pq)

            if prev_max < start:
                res.append(Interval(prev_max, start))
            prev_max = max(prev_max, schedule[idx][col].end)
            if col+1 < len(schedule[idx]):
                heapq.heappush(pq, (schedule[idx][col+1].start, idx, col+1))
        return res

z = Solution()
schedule = [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval
(2, 5), Interval(9, 12)]]
for i in z.employeeFreeTime(schedule):
    print(i.start, i.end)
