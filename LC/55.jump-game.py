class Solution(object):

    def canJump_good(self, nums):
        # Max jump keeps track of the furthest reach, since users can jump to all range(0, n) levels
        max_jump = nums[0]
        for i in range(len(nums)):

            # The current index cannot be reached
            if i > max_jump:
                return False

            # Update max_jump
            else:
                max_jump = max(max_jump, i + nums[i])
                
        return True

z = Solution()
req = [3,2,1,1,4]
print(z.canJump(req))
