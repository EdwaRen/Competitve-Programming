class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Use a deque approach, record indexes of all elements with odd values
        When k odd values reported, add the difference between the last 2
        odd indices at every iteration.
        """
        odd_numbers = [-1]
        cur_index = 0
        res = 0
        for ind, val in enumerate(nums):
            if val & 1:
                odd_numbers.append(ind)
            if len(odd_numbers) - cur_index > k + 1:
                cur_index += 1
            if len(odd_numbers) - cur_index == k + 1:
                res += odd_numbers[cur_index+1] - odd_numbers[cur_index]
        return res


z = Solution()
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(z.numberOfSubarrays(nums, k))
