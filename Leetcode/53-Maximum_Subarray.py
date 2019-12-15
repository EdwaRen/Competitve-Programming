class Solution:
    def maxSubArray(self, nums):
        cur = nums[0]
        maxsum = nums[0]
        for i in nums[1:]:
            cur = max(cur+i,i)
            maxsum = max(maxsum, cur)
        return maxsum

a = Solution()
b = [-2,1,-3,4,-1,2,-1]
print(a.maxSubArray(b))
