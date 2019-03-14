class Solution(object):
    def findUnsortedSubarray(self, nums):
        # Handle edge case
        if len(nums) == 0:
            return 0

        # Keep track of min and max value that breaks ascending order
        min_val = nums[-1]
        max_val = nums[0]

        # Detect smallest value after ascending order is broken
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                min_val = min(min_val, nums[i])

        # Detect largest value after descending order (downwards) is broken
        for i in reversed(range(len(nums)-1)):
            if nums[i] > nums[i+1]:
                max_val = max(max_val, nums[i])

        # Record index of when extremas when order was broken
        min_index = 1
        max_index = 0
        
        # Determine where the lowest broken value should have been
        for i in range(0, len(nums)):
            if nums[i] > min_val:
                min_index = i
                break
    
        # Determine where the highest broken value should have been
        for i in reversed(range(len(nums))):
            if nums[i] < max_val:
                max_index = i
                break
        #print("max val, min val, max ind, min ind", max_val, min_val, max_index, min_index)
        return max_index - min_index + 1

z = Solution()
arr = [2, 6, 1, 4, 8, 14, 10, 9, 15]
#arr = [1, 2, 4, 5]
print(z.findUnsortedSubarray(arr))


