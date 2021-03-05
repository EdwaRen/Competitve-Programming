class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Usee hash table, similar to 2-sum
        """
        prefix = {0: -1}
        cur_sum = 0
        longest = 0

        for idx, val in enumerate(nums):
            cur_sum += val
            if cur_sum - k in prefix:
                longest = max(longest, idx - prefix[cur_sum-k])
            if cur_sum not in prefix:
                prefix[cur_sum] = idx 
        return longest

z = Solution()
nums = [1, -1, 5, -2, 3]
k = 4
# nums = [-2, -1, 2, 1]
# k = 1
print(z.maxSubArrayLen(nums, k))