class Solution(object):
    def firstMissingPositive(self, nums):
        """
        Solution uses the negative method of marking numbers.
        Basically does 'if val in nums' but in-place by marking the passed-in values with negatives
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        # Mark negative numbers and numbers over n
        for index in range(n):
            if nums[index] > n or nums[index] <= 0:
                nums[index] = n + 1

        # Mark valid numbers as negative once passed through
        for index in range(n):
            val = abs(nums[index])
            if val > 0 and val <= n:
                nums[val-1] = -1 * abs(nums[val-1])

        # Check for first positive. 
        for index in range(n):
            if nums[index] > 0:
                return index +1

        return n+1
        
z = Solution()
nums = [1,1]
# nums = [1, 2, 0]
# nums = [3, 4, -1, 1]
# nums = [7,8,9,11,12]
print(z.firstMissingPositive(nums))