import itertools

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # Handle edge case
        if not nums:
            return []

        # Declare result, sort nums
        result = []
        nums_new = sorted(nums)

        # Recurse
        self.nSum(4, 0, len(nums)-1, nums_new, target, [], result)

        # Remove duplicates
        result.sort()
        return list(k for k , _ in itertools.groupby(result))

    def nSum(self, N, lo, hi, nums, target, pre, result):
        """
        Recurses by reducing n until n == 2
        Basically reducing the problem to a n-1 problem and locking previous values
        lo and hi are only for elements past 'locked' ones
        """
        # If N == 2, perform 2 sum algorithm
        if N == 2:

            # Cur_sum is the sum of the current low and hi
            # Stack_sum is the sum of everything on the stack
            cur_sum = nums[lo] + nums[hi]
            stack_sum = target - sum(pre)

            # Two pointer solution
            while lo < hi:

                # Change lo and hi based on cur_sum vs stack_sum
                if cur_sum > stack_sum:
                    hi -=1
                elif cur_sum < stack_sum:
                    lo +=1

                # Append to result
                else:
                    result.append(pre +[nums[lo], nums[hi]])
                    hi -=1

                # Update sum
                cur_sum = nums[lo] + nums[hi]

        elif N > 2:
            # Locks in element from 1 to len(nums)
            for i in range(1, hi):
                if lo + i  < len(nums):
                    self.nSum(N-1, lo+i, hi, nums, target, pre+[nums[lo+i-1]], result)

z = Solution()
nums = [-3,-2,-1,0,0,1,2,3]
print(z.fourSum(nums, 0))
