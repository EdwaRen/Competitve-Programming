import collections

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        
        Similar approach to two sum
        """
        previously_seen = collections.defaultdict(int)
        pairs = 0
        for t in time:
            time_modulo = t%60
            time_remaining = (60-time_modulo)%60
            if time_remaining in previously_seen:
                pairs += previously_seen[time_remaining]
            previously_seen[time_modulo]+=1
        return pairs

z = Solution()
time = [30, 20, 150, 100, 40]
time = [60, 60, 60]
print(z.numPairsDivisibleBy60(time))
