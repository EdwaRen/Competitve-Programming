class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0]
        dp.append(nums[0])
        dp.append(nums[1])

        for i in range(2, len(nums)):
            dp_l = len(dp)
            dp.append(nums[i] + max(dp[dp_l-2], dp[dp_l-3]))       
        return max(dp[-1], dp[-2])

z = Solution()
nums = [2, 7, 9, 3, 1]
print(z.rob(nums))
