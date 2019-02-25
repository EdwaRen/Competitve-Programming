class Solution(object):
    def rob(self, nums):
        def rob_n(nums, start, end):
            prev1 = 0
            prev2 = 0
            for i in range(start, end):
                tmp = prev1
                prev1 = max(nums[i] + prev2, prev1)
                prev2 = tmp
            return prev1
        if not len(nums):
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(rob_n(nums, 0, len(nums)-1 ), rob_n(nums, 1, len(nums)) )

z = Solution()
arr = [1, 2, 3, 1, 5]
print(z.rob(arr))
