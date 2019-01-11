from pprint import pprint
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        sorted_int = sorted(intervals, key=lambda x: x.start)
        max_len = len(sorted_int)
        index = 1
        while index < max_len:
            if index == 0:
                break
            if sorted_int[index].start <= sorted_int[index-1].end:
                if sorted_int[index-1].end < sorted_int[index].end:
                    sorted_int[index-1].end = sorted_int[index].end
                del sorted_int[index]
                index-=1
                max_len-=1
            index+=1
        return sorted_int
a = Solution()
b = a.merge([Interval(1, 4), Interval(0, 2), Interval(3, 5)])
b = a.merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)])
b = a.merge([Interval(1, 4), Interval(4, 5)])
for pair in b:
    print(pair.start, pair.end)
