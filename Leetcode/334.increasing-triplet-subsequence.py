class Solution(object):
    def increasingTriplet(self, nums):
        first = 9999999999999
        second = 9999999999999
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True

        return False

z = Solution()
nums = [5, 4, 1, 20, 3]
print(z.increasingTriplet(nums))
