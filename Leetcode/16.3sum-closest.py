class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        closest = abs((nums[0] + nums[1] + nums[2]) - target)
        res = res = [nums[0], nums[1], nums[2]]
        for i in range(len(nums)-2):
            lo = i+1
            hi = len(nums) - 1
            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]

                if abs(cur_sum - target) < (closest):
                    closest = abs(cur_sum - target)
                    res = [nums[i], nums[lo], nums[hi]]

                if cur_sum == target:
                    closest = 0
                    res = [nums[i], nums[lo], nums[hi]]
                    return sum(res)
                elif cur_sum > target:
                    hi -=1
                elif cur_sum < target:
                    lo +=1
                
        return sum(res)

z = Solution()
nums = [ 5, 1, -4, 4]
target = 0
print(z.threeSumClosest(nums, target))

        
