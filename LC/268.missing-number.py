class Solution(object):
    def missingNumber(self, nums):
        sum = 0

        # expected is found with Gauss's formula
        expected = (1 + len(nums)) * len(nums) / 2        

        # sum everything in num
        for i in nums:
            sum += i

        # The remaining number is the difference 
        return int(expected) - sum


z = Solution()
arr = [0, 1, 3]
print(z.missingNumber(arr))




