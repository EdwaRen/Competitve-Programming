class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Two pointer solution. The 'j' loop uses the indexing j value as the
        left pointer and the right-most index as the right pointer.
        """
        nums.sort()
        res = 0
        N = len(nums)

        for i in range(N):
            right = N-1
            for j in range(i+1, N):
                cur_sum = nums[i] + nums[j]
                while right >= 0 and cur_sum + nums[right] >= target:
                    right -=1
                if right > j:
                    res += right - j
                else:
                    break
        return res

z = Solution()
nums = [-2, 0, 1, 3]
target = 2
nums = [0]
target = 0
#
nums = [0, 0, 0]
target = 0
print(z.threeSumSmaller(nums, target))
