import math

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        if len(nums) > threshold:
            return -1        
        hi, lo = max(nums), 1

        # Binary Search
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if self.calculateSumDivisor(nums, mid) > threshold:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo 

    def calculateSumDivisor(self, nums, divisor):
        div_sum = 0
        for i in nums: div_sum += -(-i/divisor)
        return div_sum

z = Solution()
nums = [44,22,33,11,1]
nums = [21212,10101,12121]
nums = [2,3,5,7,11]
T = 5
T = 1000000
T = 11
print(z.smallestDivisor(nums, T))