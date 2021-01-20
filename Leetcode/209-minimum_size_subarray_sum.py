class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int

        Sliding window solution using two pointers
        """
        left, right, sliding_sum, cur_min = 0, 0, 0, float('inf')

        while left <= right:
            if sliding_sum >= s:
                cur_min = min(cur_min, right-left)
                sliding_sum -= nums[left]
                left += 1
            elif sliding_sum < s:
                if right >= len(nums): break
                sliding_sum += nums[right]
                right += 1

        return cur_min if cur_min != float('inf') else 0

z = Solution()
s = 1231
nums = [2, 3, 1, 2, 4, 3]
print(z.minSubArrayLen(s, nums))
