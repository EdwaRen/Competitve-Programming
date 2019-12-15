class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        ascents = []
        lower = prices[0]
        upper = prices[0]
        res = 0


        for i in prices:
            if i > upper:
                upper = i
            elif i < upper:
                ascents.append(upper-lower)
                res += upper-lower
                lower = i
                upper = i
        ascents.append(upper-lower)
        res += upper-lower
        # print("ascents", ascents)
        return res



a = Solution()
print(a.maxProfit([7,6,4,3,1]))
