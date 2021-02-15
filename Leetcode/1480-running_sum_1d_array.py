class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev = 0
        res = [0 for i in nums]
        for i in range(len(nums)):
            res[i] = nums[i] + prev
            prev = res[i]
        return res 

z = Solution()
nums = [3, 1, 2, 10, 1]
print(z.runningSum(nums))
