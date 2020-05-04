class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        lo = 0
        hi = len(nums) -1
        mid = (lo + hi) / 2
        if target > nums[hi]:
            return hi + 1

        while lo <= hi:
            mid = (lo + hi) / 2

            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid
        # print("low and hi", lo, hi)
        return lo

z = Solution()
nums = [1,3,5,8]
target = 9
print(z.searchInsert(nums, target))
