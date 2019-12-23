class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        def convertTime(a):
            return int(a[:2])*60 + int(a[3:])

        numPoints = sorted([convertTime(i) for i in timePoints])
        cur_min = 99999999

        for i in range(1, len(numPoints)):
            if numPoints[i] - numPoints[i-1] < cur_min:
                cur_min = numPoints[i] - numPoints[i-1]
        if (numPoints[0]+(24*60) - numPoints[-1]) < cur_min:
            cur_min = (numPoints[0]+(24*60) - numPoints[-1])
        
        return cur_min

z = Solution()
timePoints = ["23:59","00:00"]
print(z.findMinDifference(timePoints))
