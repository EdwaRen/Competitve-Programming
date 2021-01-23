import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """

        # Combine input params and sort by endTime value
        jobs = list(zip(endTime, startTime, profit))
        jobs.sort(key=lambda x:x[0])
        print(jobs)

        dp = [[0, 0]] # contains elements that are (end, current_profit)
        keys = [0] # Remember keys for bisection purposes

        # Go through all jobs and binary search for schedule that most recently completed after current start
        for e, s, p  in jobs:
            bisect_idx = bisect.bisect(keys, s)-1 # index of schedule

            # Update dp if current profit + older dp_max is bigger than the current dp_max
            if p + dp[bisect_idx][1] > dp[-1][1]: # and s >= dp[bisect_idx][0]:
                dp.append([e, p + dp[bisect_idx][1]])
                keys.append(e)

        return dp[-1][1]


z = Solution()
st = [1,2,3,3]
et = [3,4,5,6]
p = [50,10,40,70]

# st = [1, 2, 3, 4, 6]
# et = [3,5,10,6,9]
# p = [20,20,100,70,60]

# st = [1, 1, 1]
# et = [2, 3, 4]
# p = [5, 6, 4]

# st = [11,10,14,24,5,9,3,17,27,20]
# et = [20,23,22,29,9,13,9,23,28,30]
# p = [2,2,3,2,4,3,4,4,7,2]


print(z.jobScheduling(st, et, p))