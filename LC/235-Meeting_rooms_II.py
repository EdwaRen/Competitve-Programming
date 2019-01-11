# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res = 0
        j = 0
        available = 0
        for i in range(len(start)):
            while j < len(end) and end[j] <= start[i]:
                available+=1
                j+=1
            if available:
                available -=1
            else:
                res+=1
        return res

a = Solution()
b = [[0, 30],[5, 10],[15, 20]]
b = [[2, 3], [0, 4], [6, 7], [0, 9], [5, 8]]
print(a.minMeetingRooms(b))
