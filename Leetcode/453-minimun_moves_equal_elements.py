class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums)*len(nums)

z = Solution()
nums = [1, 2, 2, 4, 5]
print(z.minMoves(nums))
