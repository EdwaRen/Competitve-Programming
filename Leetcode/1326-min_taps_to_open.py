class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        Similar to jump game in a dp way. We record the max position
        that each index can jump to in O(n).
        """
        intervals = [i for i in range(len(ranges))]
        for i in range(len(ranges)):
            left, right = max(0, i - ranges[i]), min(n, i + ranges[i])
            intervals[left] = max(intervals[left], right)

        required = start = max_reach = 0
        while max_reach < n:
            required += 1
            start, max_reach = max_reach, max(intervals[i] for i in range(start, max_reach+1))
            if start == max_reach:
                return -1

        return required 
        
z = Solution()
ranges = [3,4,1,1,0,0]
n = len(ranges)-1
n = 3
ranges = [0,0,0,0]

# n = 7
# ranges = [1,2,1,0,2,1,0,1]

# n = 8
# ranges = [4,0,0,0,0,0,0,0,4]

# n = 8
# ranges = [4,0,0,0,4,0,0,0,4]
print(z.minTaps(n, ranges))
            

