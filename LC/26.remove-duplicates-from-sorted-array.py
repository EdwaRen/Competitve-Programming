class Solution(object):
    def removeDuplicates(self, nums):

        # Handle edge case
        if not nums or len(nums) == 0:
            return 0
        
        # Use crawler and runner
        left = 0
        left_run = 1
        

        # Go through all elements in num
        while left_run < len(nums):

            # If something was bigger than last biggest number, put it at the crawler index
            if nums[left_run] != nums[left]:
                left+=1
                nums[left] = nums[left_run]

            # Update runner
            left_run+=1

        return left + 1
z = Solution()
nums = [0,0,1,1,1,2,2,3,3,4, 4, 4, 4, 4, 4, 5, 6]
#nums = []
print(z.removeDuplicates(nums))
print(nums)
