class Solution(object):
    def maxProduct(self, nums):

        # Handle edge case
        if len(nums) == 1 and nums[0] < 0:
            return nums[0]

        # Keep track of current maxima and minima
        cur_max = nums[0]
        cur_min = nums[0]
        glob_max = nums[0]

        # Iterate through all nums of the array
        for i in range(1, len(nums)):

            # Swap if a negative number is found, thus when multiplied by nums[i] would reverse the pos/neg sign
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max

            # Keep current or multiply by new
            cur_max = (max(nums[i], nums[i]*(cur_max)))
            cur_min = (min(nums[i], nums[i]*(cur_min)))

            # Keep track of global maximum
            glob_max = max(cur_max, glob_max)

        # Return global max
        return glob_max

        
z = Solution()
arr = [3, -2, 4, -5, -1]
print(z.maxProduct(arr))
