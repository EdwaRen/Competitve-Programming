import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Use Counter as a frequency map. Iterate over counter to handle 
        edge case of k == 0.
        """
        seen = collections.Counter(nums)
        total = 0
        for i in seen:
            if (i-k in seen and k > 0) or (k == 0 and seen[i-k]>1):
                total += 1
        return total

z = Solution()
nums = [1,2,3,4,5]
k = 1
nums = [1,3,1,5,4]
k = 0
# nums = [1,2,4,4,3,3,0,9,2,3]
# k = 3
# nums = [-1,-2,-3]
# k = 1
print(z.findPairs(nums, k))