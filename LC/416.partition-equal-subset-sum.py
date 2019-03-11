class Solution:

    def canPartition(self, nums):
        total = sum(nums)
        half = int(total / 2)

        # Catch edge case
        if total & 1:
            return False

        # Initialize DP array
        dp = [False for i in range(half+1)]
        dp[0] = True

        for i in range(len(nums)):

            # Reverse or else all values will override the previous and be set to True
            for j in reversed(range(half+1)):

                # Catch index out of bounds
                if nums[i] <= j:
                    dp[j] = dp[j] or dp[j-nums[i]]

        return dp[half]



    def canPartitionRecurse(self, nums, index, state, dp):


        # Return true when both subsets are now empty
        if state[0] == 0 and state[1] == 0:
            return True
        # Return false when a subset becomes negative
        elif state[0] < 0 or state[1] < 0:
            return False
        elif index >= len(nums):
            return False

        # Recurse
        return self.canPartitionRecurse(nums, index+1, [state[0] - nums[index], state[1]]) or self.canPartitionRecurse(nums, index+1, [state[0], state[1] - nums[index] ])


z = Solution()
nums = [1, 5, 5, 10]
print(z.canPartition(nums))
