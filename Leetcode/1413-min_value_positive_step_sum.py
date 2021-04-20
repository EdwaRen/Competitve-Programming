class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_prefix = float('inf')
        cur_sum = 0
        for i in nums:
            cur_sum+= i
            min_prefix = min(min_prefix, cur_sum)
        return 1 if min_prefix > 0 else 1 + int(-1*min_prefix)

z = Solution()
nums = [-3,2,-3,4,2]
print(z.minStartValue(nums))
