class Solution:
    def twoSum(self, nums, target):
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            if nums[lo]+nums[hi] > target:
                hi-=1
            elif nums[lo]+nums[hi] < target:
                lo+=1
            elif nums[lo]+nums[hi] == target:
                return [lo+1, hi+1]
        return False

a = Solution()
b = [3, 7]
c = 9
print(a.twoSum(b, c))
