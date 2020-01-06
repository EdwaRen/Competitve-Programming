import random
import bisect

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        # Map weights to a cumulative frequency list
        self.cumulative = []
        self.total = 0
        for i in w:
            self.total+=i
            self.cumulative.append(self.total)


    def pickIndex(self):
        """
        :rtype: int
        """
        # Binary search through a cumulative frequency list
        rnd = random.randint(1, self.total)
        return bisect.bisect_left(self.cumulative, rnd)

w = [3, 3, 3, 3, 3, 3]  
z = Solution(w)
for _ in range(20):
    z.pickIndex()
# print(z.pickIndex())
# print(z.pickIndex())
# print(z.pickIndex())

# print(z.pickIndex())
# print(z.pickIndex())
# print(z.pickIndex())

# print(z.pickIndex())
# print(z.pickIndex())
# print(z.pickIndex())


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
