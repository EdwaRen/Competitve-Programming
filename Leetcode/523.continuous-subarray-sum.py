class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # Keep track of the sums in a set for O(1) lookups
        set_sums = set()

        # Record current sum and rev sum
        cur_sum = 0
        prev_sum = 0

        # We found a continuous subarray when the sum % k equals a previous  sum
        for i in nums:
            cur_sum = (cur_sum + i)
            if k != 0:
                cur_sum %= k

            if cur_sum in set_sums:
                return True 

            # To enforce subarrays > size 2, we add the previous sum to seen elements
            set_sums.add(prev_sum)
            prev_sum = cur_sum
        return False

z = Solution()
nums = [23, 2, 4, 6, 7]
# nums = [1, 0, 1, 0, 1]
nums = [0]
k = 0
res = z.checkSubarraySum(nums, k)
print(res)

        
