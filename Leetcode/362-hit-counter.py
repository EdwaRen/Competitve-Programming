import collections

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.queue.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
        
        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
obj = HitCounter()
obj.hit(1)
param_2 = obj.getHits(2)
print(param_2)
obj.hit(52)
obj.hit(54)
print(obj.getHits(55))
print(obj.getHits(301))

