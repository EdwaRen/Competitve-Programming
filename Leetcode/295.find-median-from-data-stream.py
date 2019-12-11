from heapq import heappush, heappop, heappushpop

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_h = [] # Elements ABOVE median, minheap
        self.max_h = [] # Elements BELOW median, maxHeap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Balance trees with heappushpop to ensure both are same size
        if len(self.min_h) == len(self.max_h):
            heappush(self.max_h, -heappushpop(self.min_h, num))
        else:
            heappush(self.min_h, -heappushpop(self.max_h, -num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_h) == len(self.max_h):
            return 0.5*(self.min_h[0] - self.max_h[0])
        else:
            return -self.max_h[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(-1)
obj.addNum(-2)
obj.addNum(-3)
obj.addNum(-4)
obj.addNum(-6)


param_2 = obj.findMedian()
print(param_2)
