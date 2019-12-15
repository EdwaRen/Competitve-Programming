import math

class Solution(object):
    def searchRange(self, nums, target):

        #search left
        l = 0
        r = len(nums)-1
        found_l = False
        while l <= r:
            mid = math.floor((l+r)/2)
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] >= target:
                if nums[mid] == target:
                    found_l=True
                r = mid -1

        left_side = l

        l = 0
        r = len(nums)-1
        while l <= r:
            mid = math.floor((l+r)/2)
            if nums[mid] <= target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid -1
        right_side = r
        if found_l:
            return[left_side, right_side]
        else:
            return[-1, -1]


z = Solution()
arr = [5,7,7,8,8,10]
target = 7
print(z.searchRange(arr, target))
