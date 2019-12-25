class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if nums == None or k == None or k == 0:
            return None 
        
        if len(nums) < 3*k:
            return []

        cur_left = sum(nums[:k])
        cur_right = sum(nums[-k:])
        left_sums = [(0, sum(nums[:k]))]
        right_sums = [(len(nums)-k, sum(nums[-k:]))]

        for i in range(k, len(nums)):
            cur_left = cur_left + nums[i] - nums[i-k]
            if cur_left > left_sums[-1][1]:
                left_sums.append((i-k+1, cur_left))
            else:
                left_sums.append(left_sums[-1])

        for i in range(len(nums)-k-1, -1, -1):
            cur_right = cur_right + nums[i] - nums[i+k]
            if cur_right >= right_sums[0][1]:
                right_sums.insert(0, (i, cur_right))
            else:
                right_sums.insert(0, right_sums[0])
        
        cur_max = 0
        cur_res = []
        cur_window = sum(nums[k:2*k])

        for i in range(k, len(nums)-(2*k)+1):
            cur_sum = cur_window + left_sums[i-k][1] + right_sums[i+k][1]
            cur_window += nums[i+k] - nums[i]
            if cur_sum > cur_max:
                cur_res = [left_sums[i-k][0], i, right_sums[i+k][0]]
                cur_max = cur_sum 

        return cur_res

z = Solution()
nums = [7,13,20,19,19,2,10,1,1,19]
k = 3
# nums = [1, 2, 1, 2, 1, 2, 1, 2, 1]
# k = 2
res = z.maxSumOfThreeSubarrays(nums, k)
print(res)


