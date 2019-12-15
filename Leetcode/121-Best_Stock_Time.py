import sys

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        minsell = prices[0]
        maxsell = prices[-1]
        res = 0
        for i in range(len(prices)):
            if prices[i] < minsell:
                minsell = prices[i]
            else:
                if prices[i] - minsell > res:
                    res = prices[i] - minsell
        return res
a = Solution()
b = [7,6,4,3,1]
b = [7,1,5,3,6,4]
print(a.maxProfit(b))
